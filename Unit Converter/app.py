import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Title
# st.title("Simple Unit Converter")

# Category Selection
st.write("# Simple Unit Converter")
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Conversion Logic
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Grams": 1,
        "Kilograms": 0.001,
        "Pounds": 0.00220462
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return ((value - 273.15) * 9/5) + 32

# Input Section
st.subheader(f"{conversion_type} Converter")
value = st.number_input("Enter Value", value=1.0)

# Unit Selection Based on Type
if conversion_type == "Length":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Miles"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Miles"])
    result = length_converter(value, from_unit, to_unit)

elif conversion_type == "Weight":
    from_unit = st.selectbox("From", ["Grams", "Kilograms", "Pounds"])
    to_unit = st.selectbox("To", ["Grams", "Kilograms", "Pounds"])
    result = weight_converter(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    result = temperature_converter(value, from_unit, to_unit)

# Display Result
st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")



