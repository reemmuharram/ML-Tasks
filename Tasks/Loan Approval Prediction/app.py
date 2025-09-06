import pandas as pd
import streamlit as st
import joblib 

model=joblib.load("model.pkl")

st.title("Loan Approval Prediction 🏦")
st.write("Applicant's details to predict loan approval:")

no_of_dependents = st.slider("Number of Dependents: ", min_value=0, max_value=5, step=1)

education = st.selectbox("Applicants Education level", ["Graduate", "Not Graduate"])
education = 1 if education == "Graduate" else 0


self_employed = st.checkbox("Is the applicant self employed?")
self_employed = 1 if self_employed else 0

income_annum = st.number_input("Enter Applicant's Annual Income: ", min_value=200*10**3, 
                               max_value=99*(10**5), 
                               step=1000, 
                               value=5*10**5)
loan_amount = st.number_input("Enter the Loan Amount: ", min_value=3*10**5, 
                              max_value = 395*10**5, 
                              step = 1000,
                              value=5*10**6)
loan_term = st.slider("Enter the Loan Term (in years): ", min_value=2, 
                      max_value=20, 
                      step=1, 
                      value=11)
cibil_score = st.number_input("Enter Applicant's Credit Card Score: ", min_value = 300, 
                              max_value=900, 
                              step=50, 
                              value=600)
residential_assets_value = st.number_input("Enter Residential Assets Vlaue: ", min_value=0, 
                                           max_value=1*10**7, 
                                           value=5*10**5,
                                           step = 1000)
commercial_assets_value = st.number_input("Enter Commerical Assets Vlaue: ", min_value=0, 
                                          max_value=194*10**5, 
                                          value=5*10**5,
                                          step = 1000)
luxury_assets_value = st.number_input("Enter Luxury Assets Vlaue: ", min_value=3*10**5, 
                                      max_value=392*10**5, 
                                      value=5*10**5,
                                      step = 1000)
bank_assets_value = st.number_input("Enter Bank Assets Vlaue: ", min_value=0, 
                                    max_value=147*10**5, 
                                    value=5*10**5,
                                    step = 1000)

if st.button("Predict"):
    data = {
    "no_of_dependents": no_of_dependents,
    "education": education,
    "self_employed": self_employed,
    "income_annum": income_annum,
    "loan_amount": loan_amount,
    "loan_term": loan_term,
    "cibil_score": cibil_score,
    "residential_assets_value": residential_assets_value,
    "commercial_assets_value": commercial_assets_value, 
    "luxury_assets_value": luxury_assets_value,
    "bank_asset_value": bank_assets_value
}

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    if prediction == 1:
        st.success("Loan Approved ✅")
    elif prediction == 0:
        st.error("Loan Rejected ❌")
