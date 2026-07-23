import streamlit as st


def dashboard(username, user_data):


    st.title(f"Welcome, {username}")

    st.divider()

    if user_data["gender"] == "Male":
        bmr = (
            13.4 * user_data["weight"]
            + 4.8 * user_data["height"]
            - 5.7 * user_data["age"]
            + 88.3
        )
    else:
        bmr = (
            9.2 * user_data["weight"]
            + 3.1 * user_data["height"]
            - 4.3 * user_data["age"]
            - 447.6
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Profile")

        st.write(f"age: {user_data['age']}")
        st.write(f"height: {user_data['height']} cm")
        st.write(f"weight: {user_data['weight']} kg")
        st.write(f"goal: {user_data['goal']}")
        st.write(f"activity level: {user_data['activity_level']}")
        st.write(f"experience: {user_data['exp']}")
        st.write(f"days per week: {user_data['days_per_week']}")

    with col2:
        st.subheader("daily recommendations")

        st.write(f"calories: {bmr:.0f} kcal")
        st.write(f"protein: {user_data['weight'] * 1.3:.0f} grams")
        st.write(f"water: {user_data['weight'] * 0.033:.1f} litres")
        st.write(f"carbs: {user_data['weight'] * 1.9:.0f} grams")
        st.write(f"fats: {user_data['weight'] * 0.8:.0f} grams")


    st.divider()

    st.divider()

    if st.button("🏋️ Workout Planner"):
        st.session_state.page = "Workout Planner"
        st.write("Navigating to Workout Planner...")
        st.rerun()

