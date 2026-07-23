import streamlit as st
import pandas as pd
import os
import register
import dashboard
import workout

st.write(dashboard.__file__)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


if st.session_state.logged_in:

    if st.session_state.page == "Dashboard":
        dashboard.dashboard(
            st.session_state.username,
            st.session_state.user_data
        )

    elif st.session_state.page == "Workout Planner":
        workout.workout_planner(
            st.session_state.user_data
        )

    st.stop()

st.logo("only.png", size="large")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("only.png", width=150)

with col2:
    st.title("MuscleMind")


tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        file = "users.csv"
        users = pd.read_csv(file)
        if username in users["username"].values:
            user_data = users[users["username"] == username].iloc[0]
            if password == user_data["password"]:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.user_data = user_data.to_dict()
                st.rerun()
            else:
                st.error("Incorrect password")
        else:
            st.error("Username does not exist")
            st.write("Please register if you don't have an account.")


with tab2:
    register.register_user()

