import streamlit as st
import requests

st.title("Movie Recommender")
user_id = st.number_input("Enter User ID (1-943):", min_value=1, max_value=943, value=1)
if st.button("Get Recommendations"):
    response = requests.get(f"http://127.0.0.1:5000/recommend?user_id={user_id}")
    if response.status_code == 200:
        data = response.json()
        st.write(f"Recommendations for User {data['user_id']}:")
        for movie in data['recommendations']:
            st.write(f"- {movie}")
    else:
        st.error(f"Error: {response.json()['error']}")
        