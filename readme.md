# **AI-Powered Medical Diagnostic Tool** 🩺
**Detect Pneumonia, COVID-19, and Lung Cancer using Machine Learning and Medical Imaging**

## 🚀 **Overview**
This project implements an AI-driven diagnostic application capable of detecting:
- **Pneumonia** and **COVID-19** from Chest X-Rays
- **Lung Cancer** from Chest CT Scans

The application combines a **Convolutional Neural Network (CNN)** for image classification with a web interface built using Django, providing an accessible and user-friendly diagnostic solution.

---

## 🛠️ **Technologies Used**

### **Machine Learning**
- **TensorFlow/Keras**: Deep learning framework for model building and training
- **NumPy**: Efficient array manipulation and computations

### **Web Development**
- **Django**: Python-based backend web framework
- **Bootstrap**: Front-end framework for responsive UI design

### **Data Preprocessing**
- **OpenCV**: Image processing for grayscale conversion, resizing, and enhancements
- **Sklearn**: For data splitting (train-test split)

---

## 🧪 **How It Works**

### **1. Data Preprocessing**
The `preprocess.py` script:
- Loads X-Ray or CT Scan images from the dataset directory.
- Converts images to grayscale and resizes them to **224x224 pixels**.
- Normalizes pixel values to the range [0, 1].
- Splits the data into training and testing sets.

```bash
# Run preprocessing to prepare the dataset
python preprocess.py
```

### **2. Model Training**
The `build_model.py` script trains a **Convolutional Neural Network (CNN)** for multi-class classification:
- 3 Classes for Pneumonia/COVID Detection: `COVID`, `Non-COVID`, and `Pneumonia`
- 2 Classes for Lung Cancer Detection: `Lung Cancer` and `Normal`

Training features include:
- **3 Convolutional Layers** with ReLU activation
- **MaxPooling** for dimensionality reduction
- **Dropout** to avoid overfitting
- **Softmax** activation for multi-class outputs

```bash
# Train the machine learning model
python build_model.py
```

### **3. Disease Detection via Web Application**
The `detect.py` file integrates the trained models into a Django web application.
- Upload chest X-Ray/CT images through the frontend.
- Process the uploaded image and predict results using the model.
- Return diagnosis (e.g., COVID, Pneumonia, or Lung Cancer) with status updates.

**Sample Workflow**:
1. Upload an image (`.jpg` or `.png`)
2. Process the image with the selected ML model.
3. Display prediction results on the UI.

---

## 🌟 **Features**
- **Multiple Disease Detection**: Predict COVID-19, Pneumonia, and Lung Cancer.
- **Responsive Web UI**: Built with Django and Bootstrap for usability.
- **Fast and Accurate Predictions**: Achieved with optimized CNN models.
- **Image Preprocessing**: Automatic image resizing and normalization for consistent results.

---

## 🖥️ **Folder Structure**

```plaintext
|-- assets/
|    |-- models/                # Pre-trained models (.h5 files)
|-- dataset/                    # Dataset of X-Ray and CT Scan images
|-- templates/                  # HTML templates for Django
|-- static/                     # Static files (CSS, JS, images)
|-- build_model.py              # ML model training script
|-- preprocess.py               # Image preprocessing script
|-- detect.py                   # Disease detection logic (Django view)
|-- requirements.txt            # Project dependencies
|-- manage.py                   # Django app manager
|-- README.md                   # Project documentation
```

---

## ⚙️ **Setup Instructions**

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/medical-diagnostic-tool.git
cd medical-diagnostic-tool
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Prepare Dataset**
Place your dataset (Chest X-Ray/CT images) in the `dataset/` folder, organized into subfolders:
```plaintext
dataset/
|-- COVID/
|-- Non-COVID/
|-- Pneumonia/
|-- Lung_cancer/
|-- Normal/
```

Run preprocessing:
```bash
python preprocess.py
```

5. **Train the Model**
```bash
python build_model.py
```

6. **Run the Web Application**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to use the application.

---

## 📊 **Results**
The CNN models achieved high accuracy on test datasets:
- **Pneumonia/COVID Detection**: Accurate classification into `COVID`, `Non-COVID`, and `Pneumonia`.
- **Lung Cancer Detection**: Effective binary classification into `Lung Cancer` or `Normal`.

---

## 👨‍💻 **Future Improvements**
- Add real-time image analysis using webcams.
- Improve accuracy with larger datasets and transfer learning.
- Deploy the application on cloud platforms for global access.

---

## 🤝 **Contributing**
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository, create a new branch, and submit a pull request.

---

## 📝 **License**
This project is licensed under the MIT License.

---

## 📫 **Contact**
For collaborations, inquiries, or feedback:
- **Name**: Farhan Basheer
- **LinkedIn**: [Farhan's LinkedIn](https://www.linkedin.com/in/farhanbasheerofficial10)
- **Email**: farhanbasheerofficial10@gmail.com

---

### **If you find this project useful, don’t forget to ⭐ star the repository!** 🌟

