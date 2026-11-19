
import streamlit as st
import cv2
import tempfile
import os
import subprocess
import imageio_ffmpeg
from ultralytics import YOLO

st.set_page_config(
    page_title="SafetyDuck AI",
    page_icon="🪖",
    layout="wide"
)

st.title("🪖 SafetyDuck AI")
st.subheader("AI-Powered Industrial Helmet Detection")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

uploaded_video = st.file_uploader(
    "Upload Construction Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_video is not None:

    st.subheader("Original Video")
    st.video(uploaded_video)

    if st.button("🚀 Start Detection"):

        input_path = None
        raw_output = None
        final_output = None
        cap = None
        writer = None

        try:
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            ) as f:
                f.write(uploaded_video.getbuffer())
                input_path = f.name

            cap = cv2.VideoCapture(input_path)

            if not cap.isOpened():
                raise RuntimeError("Unable to open uploaded video.")

            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            if fps <= 0:
                fps = 25

            raw_output = tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            ).name

            final_output = tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            ).name

            writer = cv2.VideoWriter(
                raw_output,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps,
                (width, height)
            )

            if not writer.isOpened():
                raise RuntimeError("Unable to create output video.")

            progress = st.progress(0)
            status = st.empty()

            frame_count = 0

            while True:
                ret, frame = cap.read()

                if not ret:
                    break

                results = model.predict(
                    frame,
                    imgsz=416,
                    conf=0.25,
                    verbose=False
                )

                annotated_frame = results[0].plot()
                writer.write(annotated_frame)

                frame_count += 1

                if total_frames > 0:
                    progress.progress(
                        min(frame_count / total_frames, 1.0)
                    )

                status.write(
                    f"Processing frame: {frame_count}/{total_frames}"
                )

            cap.release()
            writer.release()
            cap = None
            writer = None

            # Convert video to browser-friendly H.264
            ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

            subprocess.run([
                ffmpeg, "-y",
                "-i", raw_output,
                "-vcodec", "libx264",
                "-pix_fmt", "yuv420p",
                "-movflags", "+faststart",
                final_output
            ], check=True, capture_output=True)

            st.success("Detection completed successfully!")

            st.subheader("🎯 Helmet Detection Output")
            st.video(final_output)

            with open(final_output, "rb") as video:
                st.download_button(
                    "⬇️ Download Detected Video",
                    data=video.read(),
                    file_name="SafetyDuck_Detection.mp4",
                    mime="video/mp4"
                )

        except Exception as e:
            st.error(f"Error: {e}")

        finally:
            if cap is not None:
                cap.release()
            if writer is not None:
                writer.release()

            for path in [input_path, raw_output]:
                if path and os.path.exists(path):
                    os.remove(path)
