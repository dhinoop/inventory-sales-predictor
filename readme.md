# 🧠 Inventory Sales Prediction App

A Streamlit web app that predicts product sales for different stores based on date, holidays, and weekdays.

---

## 🚀 Live Demo

You can try the app online here:  
[**Inventory Sales Predictor - Streamlit App**](https://share.streamlit.io/<your-username>/inventory-sales-predictor/main/app/streamlit_app.py)

---
## 🚀 Features
- Predicts sales using a trained **XGBoost Regressor**
- Takes inputs for **Store ID**, **Item ID**, and **Date**
- Automatically detects weekends and Indian holidays
- Interactive and simple UI built with Streamlit

---

## 🧰 Tech Stack
- **Python**
- **Streamlit**
- **Scikit-learn**
- **XGBoost**
- **Pandas**
- **Holidays (India)**

---

## ⚙️ Setup Instructions

### 1. Clone or download this project
```bash
git clone https://github.com/your-username/inventory-sales-predictor.git
cd inventory-sales-predictor/app

```
---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Run the app

streamlit run streamlit_app.py

---

### 🧩 Example Input

| Store | Item | Date       |
| ----- | ---- | ---------- |
| 1     | 3    | 2017-03-20 |

---

### 📁 Project Structure

```

inventory_sales/                   <-- Root folder
│
├── app/                           <-- Streamlit app and trained model
│   ├── model.pkl                  <-- Saved XGBoost model
│   └── streamlit_app.py           <-- Streamlit web app script
│
├── dataset/                       <-- Raw dataset folder
│   └── inventory.csv              <-- CSV file with sales data
│
├── notebook/                       <-- Jupyter Notebook for training
│   └── model_training.ipynb        <-- Model training, feature engineering, and model save
│
├── .gitignore                     <-- To ignore .venv and temporary files
├── requirements.txt               <-- List of required Python packages
└── README.md                      <-- Project overview and instructions


```