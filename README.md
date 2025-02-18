# Automatic Number Plate Recognition System (ANPR)

## 📌 Description

The Automatic Number Plate Recognition (ANPR) System is designed to identify and read vehicle license plates from images or video streams. This project leverages image processing and machine learning techniques to detect and extract license plate information, which can be used for applications like traffic monitoring, toll collection, and security enforcement.

## 🛠 Tech Stack

- **Programming Language:** Python
- **Libraries:** OpenCV, Tesseract OCR, NumPy, Matplotlib
- **Machine Learning:** Pre-trained models for character recognition

## 🚀 Features

- ✅ **License Plate Detection:** Accurately detects license plates in various lighting and weather conditions.
- ✅ **Character Segmentation:** Isolates individual characters from the detected license plate.
- ✅ **Optical Character Recognition (OCR):** Converts segmented characters into readable text.
- ✅ **Real-time Processing:** Capable of processing video streams for live license plate recognition.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Omo-Tines/Automatic-Number-Plate-Recognition-System-ANPR-.git
   cd Automatic-Number-Plate-Recognition-System-ANPR-
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download and install Tesseract OCR:**
   - **Windows:** [Download Tesseract Installer](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS:** Install via Homebrew
     ```sh
     brew install tesseract
     ```
   - **Linux:** Install via package manager
     ```sh
     sudo apt-get install tesseract-ocr
     ```

5. **Run the application:**
   ```sh
   python main.py
   ```

## 📈 Challenges & Learnings

- **Challenge:** Achieving accurate detection under varying lighting conditions.
  - *Solution:* Implemented adaptive thresholding and image augmentation techniques to improve model robustness.

- **Challenge:** Differentiating between similar characters (e.g., 'O' and '0').
  - *Solution:* Trained the OCR model with a diverse dataset to enhance character recognition accuracy.

Through this project, I deepened my understanding of image processing, machine learning integration, and the importance of data quality in training robust models.

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance the ANPR system or fix issues, please fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📬 Contact

- **GitHub:** [Omo-Tines](https://github.com/Omo-Tines)
- **LinkedIn:** (https://www.linkedin.com/in/olaseni-towobola-683044172/)
- **Email:** olasenitowoboa@gmail.com
---

