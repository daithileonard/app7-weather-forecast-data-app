import streamlit as st
import pandas as pt

st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Week")

city = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {city}")