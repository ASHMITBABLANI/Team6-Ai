import folium
import requests

def create_map(lat, lon):

    m = folium.Map(location=[lat, lon], zoom_start=13)

    folium.Marker(
        [lat, lon],
        popup="Your Location",
        tooltip="Vehicle Location",
        icon=folium.Icon(color="blue", icon="car")
    ).add_to(m)

    return m


def predict_accident(api_url, data):

    try:
        response = requests.post(api_url, json=data)
        return response.json()

    except:
        return {"prediction": "API ERROR"}