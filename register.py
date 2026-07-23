
import streamlit as st
import pandas as pd
import os

def register_user():

    file = "users.csv"

    if not os.path.exists(file):
        df = pd.DataFrame(columns=["username", "password", "age", "gender", "height", "weight", "activity_level", "goal", "exp", "days_per_week"])
        df.to_csv(file, index=False)

    username = st.text_input("Username", key="register_username")
    password = st.text_input("Password", type="password", key="register_password")
    age=st.number_input("Age", min_value=0, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", step=1)
    weight = st.number_input("Weight (kg)")
    activity_level = st.selectbox("Activity Level",["Very low","Low", "Moderate", "High","Very High"])
    goal = st.selectbox("Main Goal",["Muscle Gain", "Fat Loss","Maintenance"])
    exp = st.selectbox("Experience",["Beginner", "Intermediate", "Advanced"])
    days_per_week = st.slider("Gym Days Per Week",1, 7, 3)

    if st.button("Register"):

        users = pd.read_csv(file)

        if username in users["username"].values:
            st.error("Username already exists")
            return
        if username == "" or password == "":
            st.error("Username and password cannot be empty")
            return
        if age <= 0:
            st.error("Age must be greater than 0")
            return

        new_user = pd.DataFrame([{"username": username,"password": password,"age": age,"gender": gender,"height": height,"weight": weight,"activity_level": activity_level,"goal": goal,"exp": exp,"days_per_week": days_per_week}])

        users = pd.concat([users, new_user], ignore_index=True)

        users.to_csv(file, index=False)

        st.success("Account created!")
