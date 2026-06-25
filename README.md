# 🏦 Credit Wise Loan Approval System

A machine learning web application that predicts whether a loan application will be approved or rejected based on applicant financial profile.

🔗 **Live App:** [https://loan-approval-system-shrajal.streamlit.app/](https://loan-approval-system-shrajal.streamlit.app/)

---

## 📌 Project Overview

This project uses a **Gaussian Naive Bayes** classification model trained on real-world inspired loan data to predict loan approval decisions. The app is built with **Streamlit** and deployed on **Streamlit Cloud**.

---

## 🚀 Features

- Predicts loan approval in real-time
- Clean and simple UI with input form
- Supports multiple applicant profiles (salaried, self-employed, unemployed)
- Covers various loan purposes (Home, Car, Education, Personal, Business)
- Shows approval/rejection result instantly

---

## 🧠 ML Pipeline

| Step | Detail |
|------|--------|
| Dataset | Custom loan dataset (1000 rows) |
| Preprocessing | NaN handling, Label Encoding, One-Hot Encoding |
| Feature Engineering | `Credit_Score²`, `DTI_Ratio²` |
| Model | Gaussian Naive Bayes |
| Accuracy | ~87% |
| Precision | ~79% |
| Recall | ~77% |

---

## 📂 Project Structure

```
credit-wise-loan/
│
├── app.py                  # Streamlit web app
├── main_model.ipynb        # ML training pipeline
├── final_loan.csv          # Preprocessed dataset
├── model.pkl               # Trained model
├── scaler.pkl              # StandardScaler
├── feature_columns.pkl     # Feature column names
├── requirements.txt        # Require library
└── README.md
```

---

## 📥 Input Features

**Numerical:**
- Applicant Income
- Co-applicant Income
- Age
- Dependents
- Existing Loans
- Savings
- Collateral Value
- Loan Amount
- Loan Term (Months)
- Credit Score (300–900)
- DTI Ratio (Debt-to-Income)

**Categorical:**
- Gender
- Employment Status
- Marital Status
- Loan Purpose
- Property Area
- Employer Category
- Education Level

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** — Data preprocessing
- **Scikit-learn** — ML model & scaling
- **Streamlit** — Web app & deployment
- **Joblib** — Model serialization

---

## ⚙️ Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/credit-wise-loan.git
cd credit-wise-loan

# 2. Install dependencies
pip install streamlit pandas scikit-learn joblib

# 3. Run the app
streamlit run app.py
```

---

## 📊 Model Training

Open `main_model.ipynb` in Jupyter Notebook and run all cells. This will generate:
- `model.pkl`
- `scaler.pkl`
- `feature_columns.pkl`

---

## 👤 Author

**Shrajal**
- 🌐 [Live App](https://loan-approval-system-shrajal.streamlit.app/)
- Built with ❤️ using Python & Streamlit
