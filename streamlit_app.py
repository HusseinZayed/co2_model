import streamlit as st
import pickle

#with open('model.pkl','rb') as f:
 # model = pickle.load(f)

st.title('CO2 Emission Prediction')

ENGINESIZE = st.number_input('Enter Engine Size',min_value=0 , max_value=100 , value=10)
CYLINDERS = st.number_input('Enter CYLINDERS',min_value=0 , max_value=100 , value=10)
FUELCONSUMPTION_CITY = st.number_input('Enter FUELCONSUMPTION_CITY',min_value=0 , max_value=100 , value=10)
FUELCONSUMPTION_HWY = st.number_input('Enter FUELCONSUMPTION_HWY',min_value=0 , max_value=100 , value=10)
FUELCONSUMPTION_COMB = st.number_input('Enter FUELCONSUMPTION_COMB',min_value=0 , max_value=100 , value=10)
FUELCONSUMPTION_COMB_MPG = st.number_input('Enter FUELCONSUMPTION_COMB_MPG',min_value=0 , max_value=100 , value=10)

#output = model.predict([[ENGINESIZE,CYLINDERS,FUELCONSUMPTION_CITY,FUELCONSUMPTION_HWY,FUELCONSUMPTION_COMB,FUELCONSUMPTION_COMB_MPG]])

#st.write(f'CO2 Emission is {output[0]}')
