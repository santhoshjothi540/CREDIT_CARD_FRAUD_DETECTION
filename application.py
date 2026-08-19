import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")
st.title("💳 Credit Card Fraud Detection Dashboard")

@st.cache_resource
def load_model():
    return joblib.load("credit_card_fraud_model.pkl")

model = load_model()

uploaded = st.file_uploader("Upload credit_card_fraud_10k.csv", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Info")
    c1,c2,c3=st.columns(3)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing", int(df.isnull().sum().sum()))

    if "is_fraud" in df.columns:
        st.subheader("Fraud Distribution")
        fig,ax=plt.subplots()
        sns.countplot(x="is_fraud",data=df,ax=ax)
        st.pyplot(fig)

        st.subheader("Correlation Heatmap")
        fig,ax=plt.subplots(figsize=(8,6))
        sns.heatmap(df.select_dtypes("number").corr(),cmap="coolwarm",ax=ax)
        st.pyplot(fig)

st.sidebar.header("Predict Transaction")

amount=st.sidebar.number_input("Amount",0.0,1000000.0,3500.0)
hour=st.sidebar.slider("Transaction Hour",0,23,14)
merchant=st.sidebar.number_input("Merchant Category (Encoded)",0,100,2)
foreign=st.sidebar.selectbox("Foreign Transaction",[0,1])
location=st.sidebar.selectbox("Location Mismatch",[0,1])
trust=st.sidebar.slider("Device Trust Score",0,100,82)
velocity=st.sidebar.number_input("Velocity Last 24h",0,100,4)
age=st.sidebar.slider("Cardholder Age",18,100,35)

if st.sidebar.button("Predict"):
    sample=pd.DataFrame({
        "amount":[amount],
        "transaction_hour":[hour],
        "merchant_category":[merchant],
        "foreign_transaction":[foreign],
        "location_mismatch":[location],
        "device_trust_score":[trust],
        "velocity_last_24h":[velocity],
        "cardholder_age":[age]
    })
    pred=model.predict(sample)[0]
    if pred==1:
        st.error("Fraudulent Transaction Detected")
    else:
        st.success("Genuine Transaction")
