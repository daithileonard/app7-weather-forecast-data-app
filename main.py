import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Week")

city = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {city}")


data = get_data((city, days, option))


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(figure)