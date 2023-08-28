# Importing the required modules
import streamlit as st
import pyrebase
from datetime import datetime

# Configeration keys
firebaseConfig = {
  "apiKey": "AIzaSyCn7-xVi0NBsRp-LIKiTFLPFXQDHqMJeo0",
  "authDomain": "buildstreamlit.firebaseapp.com",
  "projectId": "buildstreamlit",
  "databaseURL": "https://buildstreamlit-default-rtdb.firebaseio.com",
 "storageBucket": "buildstreamlit.appspot.com",
  "messagingSenderId": "549954845792",
  "appId": "1:549954845792:web:dc443ef9bc66703c949705",
  "measurementId": "G-7RF1X2RXCR"
}

# Firebase Authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db=firebase.database()
storage = firebase.storage()

st.title("Welcome to the Streamlit App")

# Authentication

choice=st.sidebar.selectbox("Select Activity",["Login","SignUp"])
email=st.sidebar.text_input("Email")
password=st.sidebar.text_input("Password",type="password")

if choice=="SignUp":
    handle=st.sidebar.text_input("Handle Name (Unique)",value="Default")
    submit=st.sidebar.button("Create Account")

    if submit:
        user=auth.create_user_with_email_and_password(email,password)
        st.success("Account Created")
        st.balloons()

        # Sign in
        user=auth.sign_in_with_email_and_password(email,password)
        db.child(user['localId']).child("handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title("Welcome "+handle)
        st.info("Go to Login Menu to Login")

