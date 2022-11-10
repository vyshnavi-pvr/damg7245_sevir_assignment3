# import requests

# import streamlit as st

# # Define the title 
# st.title("Car evaluation web application")
# st.write(
#     "The model evaluates a cars acceptability based on the inputs below.\
#     Pass the appropiate details about your car using the questions below to discover if your car is acceptable."
# )

# # Input 1
# buying = st.radio(
#     "What are your thought's on the cars buying price?",
#     ("vhigh", "high", "med", "low")
# )

# # Input 2
# maint = st.radio(
#     "What are your thoughts on the price of maintanence for the car?",
#     ("vhigh", "high", "med", "low")
# )

# # Input 3
# doors = st.select_slider(
#     "How many doors does the car have?",
#     options=["2", "3", "4", "5more"]
# )

# # Input 4
# persons = st.select_slider(
#     "How many passengers can the car carry?",
#     options=["2", "4", "more"]
# )

# # Input 5
# lug_boot = st.select_slider(
#     "What is the size of the luggage boot?",
#     options=["small", "med", "big"]
# )

# # Input 6
# safety = st.select_slider(
#     "What estimated level of safety does the car provide?",
#     options=["low", "med", "high"]
# )

# # Class values to be returned by the model 
# class_values = {
#     0: "unacceptable", 
#     1: "acceptable", 
#     2: "good", 
#     3: "very good"
#     }

# # When 'Submit' is selected
# if st.button("Submit"):

#     # Inputs to ML model
#     inputs = {
#         "inputs": [
#             {
#                 "buying": buying,
#                 "maint": maint, 
#                 "doors": doors, 
#                 "persons": persons,
#                 "lug_boot": lug_boot,
#                 "safety": safety
#             }
#         ]
#         }
        
#     # Posting inputs to ML API 
#     response = requests.post(f"http://host.docker.internal:8001/api/v1/predict/", json=inputs, verify=False)
#     json_response = response.json()

#     prediction = class_values[json_response.get("predictions")[0]]

#     st.subheader(f"This car is **{prediction}!**")


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import joblib
from PIL import Image

#app=Flask(_name_)
#Swagger(app)

# interact with FastAPI endpoint
backend = "http://api:8001/predict_model"


# pickle_in = open("../modelLinearRegression.pkl","rb")
# reg_model = joblib.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

# #@app.route('/predict',methods=["Get"])
# def predict_flashes(X_validate):
#     prediction = reg_model.predict([[X_validate]])
#     print(prediction)
#     return prediction



def main():
    st.title("Number of Flashes")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Model as a Service ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    flash_input = st.text_input("Enter Probability..X_validate","Type Here")
    result=""
    if st.button("Predict"):
        print("hello")
        # result=predict_flashes(flash_input)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='main_':
    main()
