import streamlit as st
import pandas as pd
import os

file = "users.csv"


if not os.path.exists(file):
    df = pd.DataFrame(columns=["username", "password", "age", "gender", "height", "weight", "activity_level", "goal", "exp", "days_per_week"])
    df.to_csv(file, index=False)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
age=st.number_input("Age", min_value=0, max_value=100, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
activity_level = st.selectbox("Activity Level",["Low", "Moderate", "High"])
goal = st.selectbox("Goal",["Muscle Gain", "Fat Loss", "Strength"])
exp = st.selectbox("Experience",["Beginner", "Intermediate", "Advanced"])
days_per_week = st.slider("Gym Days Per Week",1, 7, 3)

if st.button("Register"):

    users = pd.read_csv(file)

    new_user = pd.DataFrame([{"username": username,"password": password,"age": age,"gender": gender,"height": height,"weight": weight,"activity_level": activity_level,"goal": goal,"exp": exp,"days_per_week": days_per_week}])

    users = pd.concat([users, new_user], ignore_index=True)

    users.to_csv(file, index=False)

    st.success("Account created!")

