# 📩 Spam SMS Detection using Machine Learning

A Machine Learning-powered web application that classifies SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques and the **Extra Trees Classifier (ETC)** model. The application is built with **Streamlit** and containerized using **Docker** for easy deployment.

---

## 🚀 Features

* Detects whether an SMS is Spam or Not Spam
* NLP-based text preprocessing
* TF-IDF Vectorization
* High-performance Machine Learning model
* Interactive Streamlit UI
* Docker support for deployment
* Lightweight and fast predictions

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-Learn
* NLTK
* Pandas
* NumPy
* Docker

---

## 📊 Model Performance

Several machine learning models were evaluated for spam detection.

| Model                      | Accuracy   | Precision  |
| -------------------------- | ---------- | ---------- |
| K-Nearest Neighbors        | 89.65%     | 100.00%    |
| Naive Bayes                | 96.13%     | 99.07%     |
| Random Forest              | 97.00%     | 99.14%     |
| **Extra Trees Classifier** | **97.39%** | **99.17%** |

### Selected Model

✅ **Extra Trees Classifier (ETC)**

Reason:

* Highest Accuracy
* Excellent Precision
* Better overall performance compared to other models

---

## 📂 Project Structure

```text
Spam_SMS_Detection/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
│
├── Vectorizer.pkl
├── ExtraTreesClassifier.pkl
│
├── data/
│   └── spam_cleaned_nlp.csv
│
└── notebooks/
    ├── spam_detection.ipynb
    └── SMS_Detection.ipynb
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Spam_SMS_Detection.git

cd Spam_SMS_Detection
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Virtual Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux/Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t spam-sms-detector .
```

### Run Docker Container

```bash
docker run -p 8501:8501 spam-sms-detector
```

Open:

```text
http://localhost:8501
```

---

## 🧠 Machine Learning Pipeline

### Text Preprocessing

* Convert text to lowercase
* Tokenization
* Remove special characters
* Remove stopwords
* Stemming using Porter Stemmer

### Feature Engineering

* TF-IDF Vectorization

### Model Training

* Extra Trees Classifier

### Prediction

* Spam
* Not Spam (Ham)

---

## 📈 Example

### Input

```text
Congratulations! You have won a free iPhone. Click here to claim now.
```

### Output

```text
🚨 Spam Message
```

### Input

```text
Hey, are we meeting tomorrow at 10 AM?
```

### Output

```text
✅ Not Spam
```

---

## 📦 Requirements

```text
streamlit
scikit-learn
numpy
pandas
nltk
scipy
joblib
```

---

## 🎯 Future Improvements

* Bulk SMS prediction through CSV upload
* Explainable AI predictions
* Probability score visualization
* Dark mode support
* REST API integration
* Cloud deployment

---

## 👨‍💻 Author

Developed as part of a Machine Learning and NLP project to demonstrate spam detection using supervised learning techniques.

---

## 📜 License

This project is licensed under the MIT License.
