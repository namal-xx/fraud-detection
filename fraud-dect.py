import streamlit as st
import joblib
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="Fraud Detection site",
    page_icon='🚨'
    )  

st.markdown("<h2 style='text-align: center; color: #e74c3c;'>Fraud-Detection-Site</h2",unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'> Welcome to Fraud detection App!!💕</h4>",unsafe_allow_html=True)  
st.markdown("**Enter the infomation below to check whether it is fruad or not.**")  


model = joblib.load("model.pkl")     
columns = ['Age', 'AcountBalance', 'TransactionAmount', 'AnomalyScore','Hour', 'DayOfweek', 'IsWeekend', 'Logindiffhours',
      ]

# def predict_fraud(input):
#     input["Age"] = input["Age"].clip(0,100)
#     input["AcountBalance"] = input["AcountBalance"].clip(0)
#     input["TransactionAmount"] = input["TransactionAmount"].clip(0)
#     input["AnomalyScore"] = input["AnomalyScore"].clip(0,1)
#     input["Hour"] = input["Hour"].clip(0,23)
#     input["DayOfweek"] = input["DayOfweek"].clip(0,6)
#     input["IsWeekend"] = input["IsWeekend"].clip(0,1)
#     input["Logindiffhours"] = input["Logindiffhours"].clip(0,None)
   
#     return input


def parse_text(text, dtype=float):
    try:
        return dtype(text)
    except:
        return None   



col1, col2 = st.columns(2)

with col1:
    age_input = st.text_input("Enter Age." ,placeholder="e.g. 20")
    balance_input = st.text_input("Enter Account Balance.", placeholder="e.g. 12000.50")
    amount_input = st.text_input("Enter Transaction Amount.", placeholder="e.g. 46.121117")
    anomaly_input = st.text_input("Enter Anomlay score.", placeholder="e.g. 0.034059")

with col2:
    hour = st.slider("Hour of transaction (0-23).",0,23)
    day = st.selectbox("Day of week(0 = Mon, 6 = Sun).",list(range(7)))
    isweekend = st.radio("Is it weekend?",[1,0])
    login_input = st.text_input("Login Difference in Hours",placeholder="e.g.,-69.0")

age =  parse_text(age_input, int)
balance = parse_text(balance_input)
amount = parse_text(amount_input)
anomaly = parse_text(anomaly_input)
login_diff = parse_text(login_input)


if st.button("Predict"):
    try:

        if None in [age, balance, amount, anomaly, login_diff]:
            st.warning("⚠️ Please fill out all fields correctly!")
        else:
            input_data = pd.DataFrame([[
            age, balance, amount, anomaly, hour, day, isweekend, login_diff
        ]],columns=columns)
            # processed = predict_fraud(input_data)
            prediction = model.predict(input_data)

            
            if prediction[0] == 1:

              st.success('🚨 Warning! This is Fraud 🚨') 

            else:
                st.info('✅ Not Fruad!!')
                        
    except Exception as e:
        st.error(f"Something went wrong: {e}")


