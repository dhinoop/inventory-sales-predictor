import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import holidays

# -------------------------------------------------------------
# Load dataset (for reference and to populate dropdowns)
# -------------------------------------------------------------
data = pd.read_csv('../dataset/inventory.csv')
store_ids = sorted(data['store'].unique())
item_ids = sorted(data['item'].unique())

# -------------------------------------------------------------
# Load trained model
# -------------------------------------------------------------
model = joblib.load('model.pkl')

# -------------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------------
st.set_page_config(page_title="Inventory Sales Predictor", page_icon="🛒", layout="centered")

# -------------------------------------------------------------
# App Title and Description
# -------------------------------------------------------------
st.title("🛍️ Inventory Sales Prediction App")
st.write("""
Predict daily product sales for retail stores using your trained **XGBoost** model.  
Select a store, item, and date — the model will handle the rest!
""")

# -------------------------------------------------------------
# User Inputs (Dropdowns from Dataset)
# -------------------------------------------------------------
store = st.selectbox("Select Store ID", store_ids)
item = st.selectbox("Select Item ID", item_ids)
date = st.date_input("Select Date")

# Optional data preview
with st.expander("📊 View Sample Data (from training set)"):
    st.dataframe(data.head())

# -------------------------------------------------------------
# Predict Button
# -------------------------------------------------------------
if st.button("🔮 Predict Sales"):
    try:
        # Extract date features
        year, month, day = date.year, date.month, date.day
        weekend = 1 if datetime(year, month, day).weekday() > 4 else 0
        india_holidays = holidays.country_holidays('IN')
        holiday = 1 if india_holidays.get(date.strftime("%Y-%m-%d")) else 0
        weekday = datetime(year, month, day).weekday()

        # Create feature array
        features = np.array([[store, item, year, month, day, weekend, holiday, weekday]])

        # Make prediction
        prediction = model.predict(features)[0]

        st.success(f"📈 Predicted Sales: **{round(prediction, 2)}**")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

