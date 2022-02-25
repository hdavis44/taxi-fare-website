from requests.models import Response
import streamlit as st
from datetime import datetime
import requests
'''
# TaxiFareModel front
'''

date = st.date_input(
    "Choose a date",
    datetime.today()
)
st.write("You ride on ", date)

time = st.time_input(
    "Choose a time",
    datetime.now()
)
st.write("You ride at ", time)

pickup_longitude = st.number_input("Pickup longitude?", value=40.7614327)
st.write("Your pickup longitude is ", pickup_longitude)

pickup_latitude = st.number_input("Pickup latitude?", value=-73.9798156)
st.write("Your pickup latitude is ", pickup_latitude)

dropoff_longitude = st.number_input("Dropoff longitude?", value=40.6413111)
st.write("Your dropoff longitude is ", dropoff_longitude)

dropoff_latitude = st.number_input("Dropoff latitude?", value=-73.9797156)
st.write("Your dropoff latitude is ", dropoff_latitude)

passenger_count = st.slider("Select number of passengers", 1, 10, 1)
st.write(passenger_count, "passenger(s)")

url = 'https://taxifare.lewagon.ai/predict'
params = {
    'pickup_datetime': str(date) + " " + str(time),
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

if st.button('predict'):
    response = requests.get(url, params=params)
    prediction = response.json().get(round(float("prediction"),2), "no prediction")
    st.write("$", prediction)
