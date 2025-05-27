import streamlit as st

# Define conversion factors and logic
conversion_data = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
    },
    "Mass": {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 1e-6,
        "pounds": 0.453592,
        "ounces": 0.0283495
    },
    "Temperature": {
        "celsius": "c",
        "fahrenheit": "f",
        "kelvin": "k"
    },
    "Time": {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }
}

def convert_units(category, from_unit, to_unit, value):
    if category == "Temperature":
        return convert_temperature(from_unit, to_unit, value)
    else:
        base = value * conversion_data[category][from_unit]
        return base / conversion_data[category][to_unit]

def convert_temperature(from_unit, to_unit, value):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32

# --- Streamlit UI ---
st.set_page_config("Google Unit Converter", page_icon="🔁")

st.title("🔁 Unit Converter")
st.write("Convert values between Length, Mass, Temperature, and Time like Google.")

category = st.selectbox("Choose a category", list(conversion_data.keys()))

from_col, to_col = st.columns(2)

with from_col:
    from_unit = st.selectbox("From", list(conversion_data[category].keys()))
    input_value = st.number_input("Enter value", value=0.0)

with to_col:
    to_unit = st.selectbox("To", list(conversion_data[category].keys()))
    if from_unit and to_unit:
        result = convert_units(category, from_unit, to_unit, input_value)
        st.metric(label=f"{input_value} {from_unit} =", value=f"{result:.4f} {to_unit}")
