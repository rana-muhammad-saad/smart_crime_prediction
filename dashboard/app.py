import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Smart City Crime Dashboard VIP")

# Load cleaned data
df = pd.read_csv("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/data/processed/cleaned_crime_data.csv")

# Load trained model
model = joblib.load("C:/Users/BHATTI Computers/Desktop/smart_crime_prediction/models/crime_prediction_model.pkl")

# --- Crime Heatmap ---
st.subheader("Crime Heatmap")
center_lat = df["latitude"].mean()
center_lon = df["longitude"].mean()
crime_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)
heat_data = [[row["latitude"], row["longitude"]] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(crime_map)
st_data = st_folium(crime_map, width=700, height=500)

# --- Top Crime Types Graph ---
st.subheader("Top Crime Types")
fig, ax = plt.subplots(figsize=(8,5))
sns.countplot(data=df, y="crime_type", order=df['crime_type'].value_counts().index, ax=ax)
st.pyplot(fig)

# --- Crimes by Area ---
st.subheader("Crimes by Area")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.countplot(data=df, y="area", order=df['area'].value_counts().index, ax=ax2)
st.pyplot(fig2)

# --- Live Arrest Prediction ---
st.subheader("Predict Arrest Probability")
lat = st.number_input("Enter Latitude")
lon = st.number_input("Enter Longitude")

if st.button("Predict Arrest"):
    prediction = model.predict([[lat, lon]])
    if prediction[0] == 1:
        st.success("High chance of arrest at this location")
    else:
        st.info("Low chance of arrest at this location")