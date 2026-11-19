# 🪖 SafetyDuck AI – Industrial Helmet Detection using YOLO11n

**AI-Powered Industrial Safety Monitoring System**

SafetyDuck AI is a computer vision-based project that uses the YOLO11n object detection model to detect **heads, helmets, and persons** in uploaded videos. The application is built using Python and Streamlit, allowing users to upload videos, perform helmet detection, view the processed video, and download the output.

## 🚀 Live Demo

Try the application here:

[SafetyDuck AI – Live Demo](https://safetyduck-ai-helmet-detection-app-b3fk8euyxhni4wagjpqjf2.streamlit.app/)

## 📌 GitHub Repository

[SafetyDuck AI – GitHub](https://github.com/nidigallusandeep-arch/SafetyDuck-AI-helmet-detection-app)

## ✨ Features

- Upload videos in MP4, AVI, MOV, and MKV formats.
- Detect heads, helmets, and persons using YOLO11n.
- Display object detection results with bounding boxes.
- Process videos frame by frame.
- View the original and processed videos.
- Download the detected output video.
- Simple and user-friendly Streamlit interface.

## 🛠️ Technologies Used

- Python
- YOLO11n
- Ultralytics
- OpenCV
- Streamlit
- NumPy
- ImageIO-FFmpeg
- Computer Vision
- Deep Learning

## 🧠 Model Information

| Parameter | Details |
|---|---|
| Model | YOLO11n |
| Task | Object Detection |
| Framework | Ultralytics |
| Model File | best.pt |
| Classes | Head, Helmet, Person |
| Input | Image / Video |
| Output | Bounding boxes and class labels |

**Note:** The trained model detects the classes `head`, `helmet`, and `person`. It does not have a separate `no_helmet` class, so it should not be treated as a direct helmet-violation classifier.

## 📂 Project Structure

```text
SafetyDuck-AI/
│
├── app.py
├── best.pt
├── requirements.txt
├── packages.txt
└── README.md
```

## ⚙️ Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/nidigallusandeep-arch/SafetyDuck-AI-helmet-detection-app.git
```

**Step 2: Navigate to the project folder**

```bash
cd SafetyDuck-AI-helmet-detection-app
```

**Step 3: Create a virtual environment (optional)**

```bash
python -m venv venv
```

**Step 4: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 5: Run the Streamlit application**

```bash
streamlit run app.py
```

## 📋 How to Use

1. Open the SafetyDuck AI application.
2. Upload an industrial safety video.
3. Click the **Start Helmet Detection** button.
4. Wait for the video processing to complete.
5. View the processed video with detection results.
6. Download the output video.

## 🎯 Project Objective

The main objective of this project is to demonstrate how Artificial Intelligence and Computer Vision can support industrial safety monitoring by identifying people, heads, and helmets in video footage.

## 🔮 Future Improvements

- Add a dedicated no-helmet detection class.
- Improve detection accuracy.
- Add real-time webcam detection.
- Generate safety violation reports.
- Build a dashboard for safety analytics.
- Support real-time industrial safety monitoring.

## 👨‍💻 Developer

**Developed by:** Sandeep

**Project:** SafetyDuck AI – Industrial Helmet Detection

**Technologies:** Python | YOLO11n | OpenCV | Streamlit | Deep Learning

---

⭐ If you find this project useful, please consider giving the repository a star on GitHub!

**Live Demo:** https://safetyduck-ai-helmet-detection-app-b3fk8euyxhni4wagjpqjf2.streamlit.app/
