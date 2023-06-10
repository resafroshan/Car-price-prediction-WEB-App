import streamlit as st
import joblib
import numpy as np

def scaler(value,min,max):
    scaled_value = (value - min)/(max - min)
    return scaled_value

model = joblib.load('C:/Users/RESAF/Downloads/Data Science/Projects/Car price predictor/car_price.pkl')

st.title("Check your Car's Price")
    # User input values
symboling = st.text_input("Symboling")
normalized_losses = st.text_input("Normalized-losses")
num_of_doors = st.text_input("No of Doors")
wheel_base = st.text_input("Wheel Base")
length = st.text_input("Length")
width = st.text_input("Width")
height = st.text_input("Height")
curb_weight = st.text_input("Curb Weight")
num_of_cylinders = st.text_input("No of Cylinders")
engine_size = st.text_input("Engine size")
bore = st.text_input("Bore")
stroke = st.text_input("Stroke")
compression_ratio = st.text_input("Compression Ratio")
horsepower = st.text_input("Horsepower")
peak_rpm = st.text_input("Peak RPM")
city_mpg = st.text_input("City Mileage - Per Gallons")
highway_mpg = st.text_input("Highway Mileage - Per Gallons")


fuel_type = st.selectbox("Fuel Type", ['Gas', 'Diesel'])
if fuel_type == 'Gas':
    fuel_type_gas = 1
    fuel_type_diesel = 0
else:
    fuel_type_gas = 0
    fuel_type_diesel = 1

#Handling dummy variables values
aspiration = st.selectbox("Aspiration", ['Standard', 'Turbo'])
if aspiration == 'Standard':
    aspiration_std = 1
    aspiration_turbo = 0
else:
    aspiration_std = 0
    aspiration_turbo = 1
    
body_style = st.selectbox("Body Style", ['sedan', 'hatchback', 'wagon', 'hardtop', 'convertible'])
if body_style == 'sedan':
    body_style_sedan = 1
    body_style_hatchback = 0
    body_style_wagon = 0
    body_style_hardtop = 0
    body_style_convertible = 0
elif body_style == 'hatchback':
    body_style_sedan = 0
    body_style_hatchback = 1
    body_style_wagon = 0
    body_style_hardtop = 0
    body_style_convertible = 0
elif body_style == 'wagon':
    body_style_sedan = 0
    body_style_hatchback = 0
    body_style_wagon = 1
    body_style_hardtop = 0
    body_style_convertible = 0
elif body_style == 'hardtop':
    body_style_sedan = 0
    body_style_hatchback = 0
    body_style_wagon = 0
    body_style_hardtop = 1
    body_style_convertible = 0
else:
    body_style_sedan = 0
    body_style_hatchback = 0
    body_style_wagon = 0
    body_style_hardtop = 0
    body_style_convertible = 1
    
drive_wheels = st.selectbox("Drive wheels", ['Front Wheel Drive', '4 Wheel Drive', 'Rear Wheel Drive'])
if drive_wheels == 'Front Wheel Drive':
    drive_wheels_fwd = 1
    drive_wheels_4wd = 0
    drive_wheels_rwd = 0
elif drive_wheels == '4 Wheel Drive':
    drive_wheels_fwd = 0
    drive_wheels_4wd = 1
    drive_wheels_rwd = 0
else:
    drive_wheels_fwd = 0
    drive_wheels_4wd = 0
    drive_wheels_rwd = 1
    
engine_type = st.selectbox('Engine Type',['OHC', 'L', 'DOHC', 'OHCV', 'OHCF'])
if engine_type == 'OHC':
    engine_type_ohc = 1
    engine_type_l = 0
    engine_type_dohc = 0
    engine_type_ohcv = 0
    engine_type_ohcf = 0
elif engine_type == 'L':
    engine_type_ohc = 0
    engine_type_l = 1
    engine_type_dohc = 0
    engine_type_ohcv = 0
    engine_type_ohcf = 0
elif engine_type == 'DOHC':
    engine_type_ohc = 0
    engine_type_l = 0
    engine_type_dohc = 1
    engine_type_ohcv = 0
    engine_type_ohcf = 0
elif engine_type == 'OHCV':
    engine_type_ohc = 0
    engine_type_l = 0
    engine_type_dohc = 0
    engine_type_ohcv = 1
    engine_type_ohcf = 0
else:
    engine_type_ohc = 1
    engine_type_l = 0
    engine_type_dohc = 0
    engine_type_ohcv = 0
    engine_type_ohcf = 0

fuel_system = st.selectbox('Fuel System',['MPFI', '2BBL', 'MFI', '1BBL', 'IDI', 'SPDI'])
if fuel_system == 'MPFI':
    fuel_system_mpfi = 1
    fuel_system_2bbl = 0
    fuel_system_mfi = 0
    fuel_system_1bbl = 0
    fuel_system_idi = 0
    fuel_system_spdi = 0
elif fuel_system == '2BBL':
    fuel_system_mpfi = 0
    fuel_system_2bbl = 1
    fuel_system_mfi = 0
    fuel_system_1bbl = 0
    fuel_system_idi = 0
    fuel_system_spdi = 0
elif fuel_system == 'MFI':
    fuel_system_mpfi = 0
    fuel_system_2bbl = 0
    fuel_system_mfi = 1
    fuel_system_1bbl = 0
    fuel_system_idi = 0
    fuel_system_spdi = 0
elif fuel_system == '1BBL':
    fuel_system_mpfi = 0
    fuel_system_2bbl = 0
    fuel_system_mfi = 0
    fuel_system_1bbl = 1
    fuel_system_idi = 0
    fuel_system_spdi = 0
elif fuel_system == 'IDI':
    fuel_system_mpfi = 0
    fuel_system_2bbl = 0
    fuel_system_mfi = 0
    fuel_system_1bbl = 0
    fuel_system_idi = 1
    fuel_system_spdi = 0
else:
    fuel_system_mpfi = 0
    fuel_system_2bbl = 0
    fuel_system_mfi = 0
    fuel_system_1bbl = 0
    fuel_system_idi = 0
    fuel_system_spdi = 1

# Creating prediction button
if st.button("Get the Price"):
    input_data = np.array([
    [
        scaler(float(symboling), -2, 3),
        scaler(float(normalized_losses), 65, 256),
        scaler(float(num_of_doors), 2, 4),
        scaler(float(wheel_base), 86.600000, 115.600000),
        scaler(float(length), 141.100000, 202.600000),
        scaler(float(width), 60.300000, 71.700000),
        scaler(float(height), 49.400000, 59.800000),
        scaler(float(curb_weight), 1488.000000, 4066.000000),
        scaler(float(num_of_cylinders), 3.000000, 8.000000),
        scaler(float(engine_size), 61.000000, 258.000000),
        scaler(float(bore), 2.540000, 3.940000),
        scaler(float(stroke), 2.070000, 4.170000),
        scaler(float(compression_ratio), 7.000000, 23.000000),
        scaler(float(horsepower), 48.000000, 200.000000),
        scaler(float(peak_rpm), 4150.000000, 6600.000000),
        scaler(float(city_mpg), 15.000000, 49.000000),
        scaler(float(highway_mpg), 18.000000, 54.000000)
    ]
    ])

    input_data = np.concatenate([input_data, [[fuel_type_diesel, fuel_type_gas, aspiration_std, aspiration_turbo,body_style_convertible, body_style_hardtop, body_style_hatchback,
       body_style_sedan, body_style_wagon, drive_wheels_4wd,
       drive_wheels_fwd, drive_wheels_rwd, engine_type_dohc,
       engine_type_l, engine_type_ohc, engine_type_ohcf,
       engine_type_ohcv, fuel_system_1bbl, fuel_system_2bbl,
       fuel_system_idi, fuel_system_mfi, fuel_system_mpfi,
       fuel_system_spdi]]], axis=1)

    price = model.predict(input_data)
    final_price = (price[0]*(35056-5118))+5118

    # Display the predicted price
    st.write(f"EXPECTED PRICE = ${final_price.round(4)}")

