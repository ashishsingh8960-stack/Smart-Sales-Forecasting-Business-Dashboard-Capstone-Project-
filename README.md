Smart Sales Forecasting & Business Dashboard (Capstone Project)
📌 Project Overview

This capstone project is an end-to-end data science solution that analyzes sales data, predicts future sales using machine learning, and presents results through an interactive Streamlit web dashboard.
It demonstrates the complete data science lifecycle from raw data processing to model deployment.

🎯 Objectives

Analyze historical sales data

Perform feature engineering

Build a regression model to predict sales

Save and reuse trained model

Develop an interactive web dashboard using Streamlit

Provide business insights and future sales prediction

🧰 Tools & Technologies

Python

Pandas & NumPy

Scikit-learn

Joblib

Streamlit

📂 Project Structure
final-capstone-project/
│
├── data/
│   └── sales_capstone.csv
├── notebook/
│   └── sales_model.ipynb
├── model/
│   └── sales_model.pkl
├── app.py
├── README.md
└── requirements.txt

📑 Dataset Description
Column	Description
Date	Sales transaction date
Product	Product name
Category	Product category
Quantity	Units sold
Price	Price per unit
🔍 Data Preprocessing & Feature Engineering

Converted Date column to datetime

Created new feature Total_Sales = Quantity × Price

Extracted Month from date for time-based analysis

🤖 Machine Learning Model

Algorithm Used: Linear Regression

Input Features: Month, Quantity, Price

Target Variable: Total_Sales

📊 Dashboard (Streamlit)

The Streamlit dashboard allows users to:

Input Month, Quantity, and Price

Predict future sales in real time

View instant ML results in a clean web interface

🧠 Key Business Insights

Electronics category contributes the highest revenue

Sales increase over time, indicating business growth

High-value products generate major revenue share

🏁 Conclusion

This capstone project demonstrates an end-to-end machine learning workflow with deployment-ready thinking.
It strengthened my skills in EDA, feature engineering, regression modeling, and dashboard creation.

🚀 How to Run the Project

Clone the repository

Install dependencies:

pip install pandas numpy scikit-learn joblib streamlit


Train model:

jupyter notebook notebook/sales_model.ipynb


Run dashboard:

streamlit run app.py

📌 Author

Ashish Singh

⭐ If you like this project, feel free to star the repository!
