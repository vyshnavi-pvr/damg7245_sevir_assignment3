import numpy as np
import pandas as pd
import joblib

import api.predict_model

import streamlit as st
from PIL import Image

import requests


# interact with FastAPI endpoint

backend = "http://api:8001/predict_model"




pickle_in = open("modelLinearRegression.pkl","rb")

reg_model = joblib.load(pickle_in)



#@app.route('/')

def welcome():

    return "Welcome All"



#@app.route('/predict',methods=["Get"])

def predict_flashes(X_validate):

    prediction = reg_model.predict([[X_validate]])

    print(prediction)

    return prediction





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
        result= requests.get(f"http://api:8001/users/me/predict/")

        result=predict_flashes(flash_input)

    st.success('The output is {}'.format(result))

    if st.button("About"):

        st.text("Lets LEarn")

        st.text("Built with Streamlit")


# if st.button("Style Transfer"):
       
#         res = requests.get(f"http://api:8001/{style}", params=files)
#         img_path = res.json()
#         image = Image.open(img_path.get("name"))
#         st.image(image, width=500)


if __name__=='__main__':

    main()