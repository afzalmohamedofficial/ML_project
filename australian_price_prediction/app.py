import streamlit as st
import pandas as pd
import pickle
import json

with open("/mount/src/ml_project/australian_price_prediction/vehicle4.pkl", "rb") as file:
  model = pickle.load(file)


# streamlit interface
st.title("Australian Vehicle Price Prediction")

brandmapping_path = "/mount/src/ml_project/australian_price_prediction/brand_mapping.json"

with open(brandmapping_path, "r") as file:
  brands_dict = json.load(file)


st.sidebar.header("Input Features")


kilometer = st.number_input("Kilometer driven", min_value=0)
seats = st.selectbox("Select seats_count", [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 11, 12.0, 14.0, 15.0, 22.0])
Engine_in_litre = st.number_input("Engine Capacity (in L)", min_value=0.1)
Cylinders_in_engine = st.selectbox('Select Cylinders in engine', [2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0])
FuelConsumption_Per100km = st.number_input('Fuel Consumption (L/100km)', min_value=0.0)
drive_type = st.selectbox('Drive Type', ['4WD', 'AWD', 'Front', 'Rear', "Other"])
transmission = st.selectbox('Transmission', ['Automatic', 'Manual'])
vechile_history = st.selectbox("Vehicle History", ["NEW", "USED", "DEMO"])
FuelType = st.selectbox("Fuel Type", ["Diesel", "Electric", "Hybrid", "LPG", "Leaded", "Premium", "Unleaded", "Other"])
BodyType = st.selectbox("Body Type", ["Commercial", "Convertible", "Coupe", "Hatchback", "People Mover", "SUV", "Sedan", "Ute / Tray", "Wagon", "Other"])
brand_selected = st.selectbox("Select Brand", list(brands_dict.keys()))
brand_code = brands_dict[brand_selected]

input_data = {
    "Kilometres":[kilometer],
    "Seats_count":[seats],
    "Engine_in_litre":[Engine_in_litre],
    "Cylinders_in_engine":[Cylinders_in_engine],
    "FuelConsumption_Per100km":[FuelConsumption_Per100km],
    "DriveType_4WD": [1 if drive_type=="4WD" else 0],
    "DriveType_AWD": [1 if drive_type=="AWD" else 0],
    "DriveType_Front": [1 if drive_type=="Front" else 0],
    "DriveType_Other": [1 if drive_type=="Other" else 0],
    "DriveType_Rear": [1 if drive_type=="Rear" else 0],
    "Transmission_Automatic": [1 if transmission=="Automatic" else 0],
    "Transmission_Manual": [1 if transmission=="Manual" else 0],
    "vechile_history_DEMO": [1 if vechile_history=="DEMO" else 0],
    "vechile_history_NEW": [1 if vechile_history=="NEW" else 0],
    "vechile_history_USED": [1 if vechile_history=="USED" else 0],
    "FuelType_Diesel": [1 if FuelType=="Diesel" else 0],
    "FuelType_Electric": [1 if FuelType=="Electric" else 0],
    "FuelType_Hybrid": [1 if FuelType=="Hybrid" else 0],
    "FuelType_LPG": [1 if FuelType=="LPG" else 0],
    "FuelType_Leaded": [1 if FuelType=="Leaded" else 0],
    "FuelType_Other": [1 if FuelType=="Other" else 0],
    "FuelType_Premium": [1 if FuelType=="Premium" else 0],
    "FuelType_Unleaded": [1 if FuelType=="Unleaded" else 0],
    "BodyType_Commercial": [1 if BodyType=="Commercial" else 0],
    "BodyType_Convertible": [1 if BodyType=="Convertible" else 0],
    "BodyType_Coupe": [1 if BodyType=="Coupe" else 0],
    "BodyType_Hatchback": [1 if BodyType=="Hatchback" else 0],
    "BodyType_Other": [1 if BodyType=="Other" else 0],
    "BodyType_People Mover": [1 if BodyType=="People Mover" else 0],
    "BodyType_SUV": [1 if BodyType=="SUV" else 0],
    "BodyType_Sedan": [1 if BodyType=="Sedan" else 0],
    "BodyType_Ute / Tray": [1 if BodyType=="Ute / Tray" else 0],
    "BodyType_Wagon": [1 if BodyType=="Wagon" else 0], 
    "Brands": [brand_code]

}

# convert input data into dataframe
user_input = pd.DataFrame(input_data)

if st.button("Predict"):
    try:
        predicted_price = model.predict(user_input)
        st.write(f"Predicted Vehicle Price: ${predicted_price[0]:,.2f}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
