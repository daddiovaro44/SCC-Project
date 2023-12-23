import streamlit as st
from joblib import load
import pandas as pd
from PIL import Image
import csv

# @st.cache_data
def load_model(model_path):
    model = load(model_path)
    return model

def inference(row, model, feat_cols):
    features = pd.DataFrame([row], columns = feat_cols)
    
    # prediction = int(model.predict(features))
    prediction = model.predict(features)
    prediction = int(prediction.item(0))
    
    if prediction == 0:
        return 'SOFT'
    elif prediction == 1:
        return 'MEDIUM'
    elif prediction == 2:
        return 'HARD'
    elif prediction == 3:
        return 'INTERMEDIATE'
    elif prediction == 4:
        return 'HARD'

st.title('Formula 1 Tyre Compound Prediction App')
st.write('Data are collected from https://github.com/theOehrly/Fast-F1/tree/master?tab=readme-ov-file')

st.video('https://www.youtube.com/watch?v=3BEHQEiDgW0')

st.write('Please fill in elements in the side bar')

# [Compound] TyreLife,Position,GridPosition,Round,Year,AirTemp,Humidity,Pressure,Rainfall,TrackTemp,WindSpeed

laps = [str(x) for x in range(0, 15)]
positions = [str(x) for x in range(1, 21)]

tyrelife = st.sidebar.selectbox('Choose tyre age', laps)
position = st.sidebar.selectbox('Choose finish grid position', positions)
gridposition = st.sidebar.selectbox('Choose starding grid position', positions)

year = st.sidebar.selectbox('Choose year', ('2019', '2020', '2021', '2022', '2023'))

gran_prix = pd.read_csv('./data/gran_prix.csv')
races = gran_prix[year]
round_name = st.sidebar.selectbox('Choose race', races)
round = (gran_prix.index[gran_prix[year]==round_name]+1).item()

airtemp = st.sidebar.slider('Air temperature in Celsius', min_value=1.0, max_value=40.0, value=35.5, step=0.1)
humidity = st.sidebar.slider('Humidity %', min_value=0.0, max_value=100.0, step=0.1)
pressure = st.sidebar.slider('Pressure in mbar', min_value=900.0, max_value=1100.0, step=0.1)

rain = int(st.sidebar.checkbox('Rain'))

tracktemp = st.sidebar.slider('Track temperature in Celsius', min_value=10.0, max_value=60.0, value=35.5, step=0.1)
windspeed = st.sidebar.slider('Wind spee in m/s', min_value=1.0, max_value=10.0, step=0.1)

row = [tyrelife, position, gridposition, round, year, airtemp, humidity, pressure, rain, tracktemp, windspeed]

if (st.button('Guess Tyre to Start the race with')):
    feat_cols = ['TyreLife', 'Position', 'GridPosition', 'Round', 'Year', 'AirTemp', 
                 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindSpeed']

    model = load_model('./models/logisticregression.joblib')
    result = inference(row, model, feat_cols)
    st.write(result)
