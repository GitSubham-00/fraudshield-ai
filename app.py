import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('fraud_model.pkl')

st.set_page_config(page_title="Online Payment Fraud Detection", page_icon="💳", layout="centered")
st.title("💳 Online Payment Fraud Detection")
st.markdown("This app predicts whether a transaction is **fraudulent or legitimate** based on key transaction details.")

# --- Input Section ---
step = st.number_input("🕒 Step (Transaction Time Step)", min_value=1, step=1)
amount = st.number_input("💰 Transaction Amount ($)", min_value=0.0, step=0.01)
oldbalanceOrg = st.number_input("🏦 Old Balance (Origin)", min_value=0.0, step=0.01)
newbalanceOrig = st.number_input("💳 New Balance (Origin)", min_value=0.0, step=0.01)
oldbalanceDest = st.number_input("🏧 Old Balance (Destination)", min_value=0.0, step=0.01)
newbalanceDest = st.number_input("💳 New Balance (Destination)", min_value=0.0, step=0.01)
type_ = st.selectbox("📂 Transaction Type", ["CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])

# --- Encode type exactly like training ---
type_encoded = {
    "CASH_OUT": [1, 0, 0, 0],
    "DEBIT": [0, 1, 0, 0],
    "PAYMENT": [0, 0, 1, 0],
    "TRANSFER": [0, 0, 0, 1],
}[type_]

# --- Match model feature order ---
input_data = pd.DataFrame([[
    step, amount, oldbalanceOrg, newbalanceOrig,
    oldbalanceDest, newbalanceDest,
    *type_encoded
]], columns=[
    'step', 'amount', 'oldbalanceOrg', 'newbalanceOrig',
    'oldbalanceDest', 'newbalanceDest',
    'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'
])

# --- Prediction ---
if st.button("🔍 Predict Fraud"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ **This transaction is likely FRAUDULENT!**")
    else:
        st.success("✅ **This transaction seems legitimate.**")

st.markdown("---")
st.markdown("Developed by **Subham Maity** | Data Analyst | [GitHub](https://github.com/yourusername)")
