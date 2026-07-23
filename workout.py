import streamlit as st



workouts = {
        "Beginner": {
            "Muscle Gain": {
                "Full Body": [
                    "squats/extensions - 3 sets, 6-8 reps",
                    "bench/pushups - 2 sets, 6-8 reps",
                    "chest flies - 2 sets, 8-10 reps",
                    "pullups/pulldowns - 3 sets, 8 reps",
                    "bicep curls - 3 sets, 8 reps",
                    "pushdowns - 3 sets, 8 reps",
                    "leg curls - 3 sets, 6-8 reps",
                ],
            "Upper Body": [
                    "bench/pushups - 3 sets, 6-8 reps",
                    "chest flies - 2 sets, 8-10 reps",
                    "pullups/pulldowns - 2 sets, 8 reps",
                    "rows - 1-2 sets, 8 reps",
                    "bicep curls - 3 sets, 8 reps",
                    "pushdowns - 3 sets, 8 reps",
                ],
            "Lower Body": [
                    "squats/extensions - 4 sets, 6-8 reps",
                    "leg curls - 3 sets, 6-8 reps",
                    "calf raises - 3 sets, 8-10 reps",
                ],
            },
            "Fat Loss": {
                "Full Body": [
                    "squats - 3 sets x 12 reps",
                    "pushups - 3 sets x 15 reps",
                    "row machine - 3 sets x 12 reps",
                    "walking lunges - 3 sets x 12 reps"
                ]
            }
        },
        "Intermediate": {
            "Muscle Gain": {
                "Full Body": [
                    "squats/extensions - 4 sets, 6 reps",
                    "dumbell/barbell bench - 3 sets, 6 reps",
                    "incline press - 3 sets, 6-8 reps",
                    "pullups/pulldowns - 3 sets, 6 reps",
                    "bicep curls - 3 sets, 6 reps",
                    "pushdowns - 3 sets, 6 reps",
                    "rdls/leg curls - 4 sets, 6 reps",
                ],
            },
            "Fat Loss": {
                "Full Body": [
                    "squats - 4 sets x 12 reps",
                    "pushups - 4 sets x 15 reps",
                    "row machine - 4 sets x 12 reps",
                    "walking lunges - 4 sets x 12 reps"
                ]
            }
        },
        "Advanced": {
            "Muscle Gain": {
                "Full Body": [
                    "squats/extensions - 4 sets, 4-8 reps",
                    "bench/pushups - 3 sets, 4-8 reps",
                    "chest flies - 2 sets, 8 reps",
                    "pullups/pulldowns - 3 sets, 6 reps",
                    "rdls - 4 sets, 6-8 reps",
                    "bicep curls - 3 sets, 6 reps",
                    "pushdowns - 3 sets, 6 reps",
                ],
            },
            "Fat Loss": {
                "Full Body": [
                    "squats - 5 sets x 12 reps",
                    "pushups - 5 sets x 15 reps",
                    "row machine - 5 sets x 12 reps",
                    "walking lunges - 5 sets x 12 reps"
                ]
            }
        }
}   

def workout_planner(user_data):

    if st.button("⬅️ Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

    st.title("workout planner")
    st.write(
        f"Your plan is personalised for: **{user_data['goal']}** "
        f"({user_data['exp']} level)"
    )
    experience = user_data["exp"]
    goal = user_data["goal"]

    if experience in workouts:
    
        available_workouts = workouts[experience][goal]

        workout_type = st.selectbox(
            "choose workout:",
            available_workouts.keys()
        )

        st.subheader(workout_type)

        exercises = available_workouts[workout_type]


        for exercise in exercises:
            st.write(exercise)

    else:
        st.error("no workout plan available.")
