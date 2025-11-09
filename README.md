# 🚀 **FraudShield AI: Intelligent Detection of Financial Transaction Anomalies**

### 🧠 *A Machine Learning–powered Streamlit web application that detects fraudulent online payment transactions in real time.*

This project applies **AI techniques** to analyze transactional patterns and classify transactions as **fraudulent or legitimate** based on behavioral and financial attributes.

---

## 🧠 Overview
Online payment fraud poses a major challenge to digital financial systems.  
This project leverages **supervised Machine Learning algorithms** such as **XGBoost** and **Random Forest** to identify fraudulent transactions using transactional data.  
The model is integrated into a **Streamlit web app** for interactive real-time predictions.

---

## ⚙️ Tech Stack
- **Language:** Python 🐍  
- **Framework:** Streamlit  
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Joblib, Matplotlib, Seaborn  
- **Model:** XGBoost Classifier  
- **Deployment:** Streamlit Cloud  

---

## 📊 Features
✅ Detects fraudulent transactions using trained ML model  
✅ User-friendly web interface built with Streamlit  
✅ Real-time input form for transaction details  
✅ Option to upload CSV file for bulk predictions  
✅ High accuracy with explainable ML model  
✅ Fully deployable on Streamlit Cloud  

---

## 🧩 Project Workflow

### 1️⃣ Data Preprocessing
- Loaded dataset from Kaggle (Online Payment Fraud Detection).  
- Cleaned data and encoded categorical variables.  
- Split dataset into training and testing sets.  

### 2️⃣ Model Training
- Compared multiple algorithms (Logistic Regression, Random Forest, XGBoost).  
- Evaluated model using **ROC-AUC** and **F1-Score**.  
- Saved trained model as `fraud_model.pkl` using Joblib.  

### 3️⃣ Streamlit Web App
- Interactive form for users to input transaction data.  
- Real-time fraud prediction results with color-coded output.  

### 4️⃣ Deployment
- Hosted on Streamlit Cloud for public access.  

---

## 🧠 Example Input Parameters

| Feature | Description |
|----------|--------------|
| step | Transaction time step (hours) |
| amount | Transaction amount |
| oldbalanceOrg | Sender’s balance before transaction |
| newbalanceOrig | Sender’s balance after transaction |
| oldbalanceDest | Receiver’s balance before transaction |
| newbalanceDest | Receiver’s balance after transaction |
| type | Transaction type (CASH_OUT, DEBIT, PAYMENT, TRANSFER) |

---

## 🧮 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 99.7% |
| Precision | 0.94 |
| Recall | 0.91 |
| ROC-AUC | 0.997 |
---

## 🖥️ Local Setup

#### Clone the repository
```bash
git clone https://github.com/subham-maity/fraud-detection-streamlit.git
cd fraud-detection-streamlit
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Run the app locally
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Deployment on Streamlit Cloud

1. Push your project to a **public GitHub repository**.  
2. Visit [https://share.streamlit.io](https://share.streamlit.io).  
3. Connect your GitHub account and deploy the app.  
4. Choose:  
   - **Repository:** `subham-maity/fraud-detection-streamlit`  
   - **Branch:** `main`  
   - **Main file path:** `app.py`  
5. Wait for it to build, then access your public app URL (e.g.):
   ```
   https://subham-maity-fraud-detection.streamlit.app
   ```

---

## 📁 Project Structure

```
fraud-detection-streamlit/
│
├── app.py                 # Streamlit web app
├── fraud_model.pkl        # Trained XGBoost model
├── requirements.txt       # Project dependencies
├── new_file.csv           # Sample dataset (optional)
└── README.md              # Project documentation
```

---

## 👨‍💻 Contributors

| Name | Role |
|------|------|
| **Subham Maity** | ML Model Development, Web App Integration |
| **Sourav Karan** | Data Preprocessing, Testing |
| **Soumyadeep Maity** | Frontend Interface & Visuals |
| **Ettaja Hoque** | Documentation & Deployment |
| **Guide:** *Mr. Raihan Mistry* – Brainware University |

---

## 🧾 License
This project is developed as part of the **B.Tech (CSE – AIML & DS)** curriculum at **Brainware University** and is intended for academic and learning purposes.

---

## 🌟 Acknowledgement
Special thanks to our guide **Mr. Raihan Mistry** for his guidance, encouragement, and expertise in helping us complete this project successfully.
