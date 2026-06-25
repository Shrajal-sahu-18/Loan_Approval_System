import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("🏦 Credit Wise Loan Approval System")

with st.expander("ℹ️ Know This Terms"):
    st.write("""
    Dependents: Family members financially dependent on you.
    
    Existing Loans: Number of loans already running.
    
    Savings: Total savings amount.
    
    Collateral Value: Value of asset/property used as security.
    
    Credit Score: Usually between 300 and 900.
    
    DTI Ratio: Debt To Income Ratio.
    Example: EMI ÷ Monthly Income
     """)

#Numeric output
applicant_income = st.number_input("Applicant Income", min_value = 0.0)
coapplicant_income = st.number_input("Coapplicant_Income",min_value = 0.0)
age = st.number_input("Age",min_value = 18,max_value = 100)
dependents = st.number_input("Dependents",min_value = 0)
existing_loans = st.number_input("Existing Loans",min_value = 0)
savings = st.number_input("Savings",min_value = 0.0)
collateral_value = st.number_input("Collateral_value",min_value = 0.0)
loan_amount = st.number_input("Loan Amount",min_value = 0.0)
loan_term = st.number_input("Loan Term(Months)",min_value = 1)

credit_score = st.number_input("Credit Score",min_value = 300,max_value = 900)
dti_ratio = st.number_input("DTI Ratio",min_value = 0.0 ,value = 0.30)

#Dropdown
gender = st.selectbox(
    "Gender",
    ["Female","Male"]
)

employment_status = st.selectbox(
    "Employment Status",
    ["Salaried","Self-employed","Unemployed","Contract"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Married","Single"]
)

loan_purpose = st.selectbox(
    "Loan Purpose",
    ["Car","Education","Home","Personal","Buisness"]
)

property_area = st.selectbox(
    "Property_Area",
    ["Rural","Semiurban","Urban"]
)

employer_category = st.selectbox(
    "Employer Category",
    ["Government","MNC","Private","Unemployed","Business"]
)

education_level = st.selectbox(
    "Education Level",
    ["Graduate","Non Graduate"]
)

#predict
if st.button("Predict Loan Approval"):
    input_df = pd.DataFrame([[0] * len(feature_columns)], columns = feature_columns)
    #numeric columns
    input_df["Applicant_Income"] = applicant_income
    input_df["Coapplicant_Income"] = coapplicant_income
    input_df["Age"] = age
    input_df["Dependents"] = dependents
    input_df["Existing_Loans"] = existing_loans
    input_df["Savings"] = savings
    input_df["Collateral_Value"] = collateral_value
    input_df["Loan_Amount"] = loan_amount
    input_df["Loan_Term"] = loan_term
    input_df["Education_Level"] = education_level

    #feature engineering
    input_df["Credit_Score_sq"] = credit_score ** 2
    input_df["DTI_Ratio_sq"] = dti_ratio ** 2

    # Gender
    if gender == "Male":
        input_df["Gender_Male"] = 1
    
    #Employement Status
    if employment_status == "Salaried":
        input_df["Employment_Status_Salaried"] = 1
    elif employment_status == "Self-employed":
        input_df["Employment_Status_Self-employed"] = 1
    elif employment_status == "Unemployed":
        input_df["Employment_Status_Unemployed"] = 1
    
    #Marital Status
    if marital_status == "Single":
        input_df["Marital_Status_Single"] = 1
    
    #Loan purpose
    if loan_purpose == "Car":
        input_df["Loan_Purpose_Car"] = 1
    elif loan_purpose == "Education":
        input_df["Loan_Purpose_Education"] = 1
    elif loan_purpose == "Home":
        input_df["Loan_Purpose_Home"] = 1
    elif loan_purpose == "Personal":
        input_df["Loan_Purpose_Personal"] = 1 
    #Property area
    if property_area == "Semiurban":
        input_df["Property_Area_Semiurban"] = 1
    elif property_area == "Urban":
        input_df["Property_Area_Urban"] = 1
    
    #Employer Category
    if employer_category == "Government":
        input_df["Employer_Category_Government"] = 1
    elif employer_category == "MNC":
        input_df["Employer_Category_MNC"] = 1
    elif employer_category == "Private":
        input_df["Employer_Category_Private"] = 1
    elif employer_category == "Unemployed":
        input_df["Employer_Category_Unemployed"] = 1

    #Education level
    if education_level == "Non Graduate":
        input_df["Education_Level"] = 1
    else:
        input_df["Education_Level"] = 0
    
    

    #Scale
    scaled_data = scaler.transform(input_df)

    #Predict
    predict = model.predict(scaled_data)


    if predict[0] == 1: # [0] ka mtlb array ka first element preidct return karta hai array[0] array[1] to uske 0 index ki value print karta hai 
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    
   



    
    

    

