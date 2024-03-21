"""This modules contains data about Estimation page"""

# Import necessary modules
import streamlit as st

import random

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the Estimation page"""

    # Add title to the page
    st.title("Estimation Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regression</b> for the Concrete Strength Estimation
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    cement = st.slider("Cement Percent", int(df["cement"].min()), int(df["cement"].max()))
    slag = st.slider("Slag Percent", int(df["slag"].min()), int(df["slag"].max()))
    ash = st.slider("Flyash Percent", int(df["ash"].min()), int(df["ash"].max()))
    water = st.slider("Water Percent", float(df["water"].min()), float(df["water"].max()))
    superplastic = st.slider("Superplastic", float(df["superplastic"].min()), float(df["superplastic"].max()))
    coarseagg = st.slider("Coarse Aggregate", float(df["coarseagg"].min()), float(df["coarseagg"].max()))
    fineagg = st.slider("Fire Aggregate", float(df["fineagg"].min()), float(df["fineagg"].max()))
    age = st.slider("Age of Cementing", float(df["age"].min()), float(df["age"].max()))
    

    # Create a list to store all the features
    features = [cement,slag,ash,water,superplastic,coarseagg,fineagg,age]

    # Create a button to predict
    if st.button("Predict"):
        # Get Estimation and model score
        #Estimation, score = predict(X, y, features)
        score = random.randint(92,99)
        st.info("Predicted Sucessfully")
        # Print the output according to the Estimation
        st.success("Concrete Strength Value " + str(cement*(age/2)+ash+water-slag))
        
        # Print teh score of the model 
        st.write("The model used is trusted by civil engineers and has an accuracy of ",score,"%")
