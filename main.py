import streamlit as st
import plotly.express as px
from backend import get_data

# st.set_page_config(layout="wide")
st.title("Weather Forecast for the Next Week")
city = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {city}")

try:
    if city:
        filtered_data = get_data(city, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            # tempCent = [int(x) / 10 for x in temperatures]

            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (c)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)

except KeyError:
    st.error("Please enter a valid city")