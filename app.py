import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import streamlit as st
data = pd.read_csv("C:\\Users\\ashmi\\Downloads\\aiproject_with_speeds.csv")
X = data.drop("Accident_Severity", axis=1)
y = data["Accident_Severity"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = GradientBoostingClassifier(
    n_estimators=20, learning_rate=0.1, max_depth=3, random_state=42
)
model.fit(X_train, y_train)
st.title("Accident Severity Prediction with Map")
log = st.number_input("Longitude", value=77.0)
lat = st.number_input("Latitude", value=28.0)
time = st.number_input("Time of Day (1-Morning 2-Afternoon,3-Evening,4-Night]", value=2)
speed = st.number_input("Speed Limit", value=60)
uspeed = st.number_input("Vehicle Speed", value=50)
vnum = st.number_input("Number of Vehicles", value=1)
vtype = st.number_input("Vehicle Type[1-Truck 2-Bike, 3-Car 4-Auto]", value=1)
if st.button("Predict Severity"):
    data_input = pd.DataFrame({
        "longitude": [log],
        "latitude": [lat],
        "Time_of_Day": [time],
        "Speed_Limit": [speed],
        "Speed_Vehical": [uspeed],
        "Number_of_Vehicles": [vnum],
        "Vehicle_Type": [vtype]
    })
    data_scaled = scaler.transform(data_input)
    prediction = model.predict(data_scaled)
    if prediction[0] == 0:
        severity = "Minor/No Accident"
        color = "green"
    elif prediction[0] == 1:
        severity = "Major"
        color = "orange"
    elif prediction[0] == 2:
        severity = "Fatal"
        color = "red"
    else:
        severity = "Unknown"
        color = "blue"

    st.success(f"Prediction: {severity}")
    m = folium.Map(location=[lat, log], zoom_start=14)
    folium.Marker(
        location=[lat, log],
        popup=f"Severity: {severity}\nSpeed: {uspeed}\nVehicles: {vnum}\nType: {vtype}",
        icon=folium.Icon(color=color)
    ).add_to(m)
    st.components.v1.html(m._repr_html_(), height=500)
