import streamlit as st
from streamlit_folium import st_folium
import folium
from utils import create_map, predict_accident
from config import BACKEND_URL

st.set_page_config(page_title="AI Accident Prediction", layout="wide")

st.title("🚗 AI Accident Prediction Dashboard")
st.write("Predict accident risk using vehicle speed and location")

# Sidebar Inputs
st.sidebar.header("Vehicle Inputs")

speed = st.sidebar.slider("Vehicle Speed", 0, 150, 60)

lat = st.sidebar.number_input("Latitude", value=28.6692)
lon = st.sidebar.number_input("Longitude", value=77.4538)

predict_button = st.sidebar.button("Predict Accident Risk")

# Map
st.subheader("Vehicle Location")

map_obj = create_map(lat, lon)

st_folium(map_obj, width=900, height=500)

# Prediction
if predict_button:

    data = {
        "speed": speed,
        "latitude": lat,
        "longitude": lon
    }

    result = predict_accident(BACKEND_URL, data)

    st.subheader("Prediction Result")

    prediction = result.get("prediction", "UNKNOWN")

    if prediction == "HIGH":
        st.error("⚠ HIGH Accident Risk")

    elif prediction == "MEDIUM":
        st.warning("⚠ MEDIUM Accident Risk")

    else:
        st.success("SAFE")
