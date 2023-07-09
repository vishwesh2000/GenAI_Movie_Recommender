import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import json



st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/2387532/pexels-photo-2387532.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


# Load the users from the JSON file
with open("users.json", "r") as file:
    users = json.load(file)

def login(users):
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.success("Login successful. Welcome, {}!".format(username))
            switch_page('home') # Default/manual recommendation purely based on Similarity ML model.
        else:
            st.error("Invalid username or password.")

st.markdown("<h1 style='text-align: center;'>TeleGenAIsis🤖</h1>", unsafe_allow_html=True)
st.markdown("""<b><i>Welcome to TeleGenAIsis! 🌟✨ Immerse yourself in a personalized OTT experience like never before. 
Our fusion of generative AI and telepathic wonders unlocks a world of enchantment. 🧙‍♀️🔮 Explore shows, movies, 
and documentaries tailored to your wildest dreams, with unexpected plot twists and mind-bending endings. 🌪️🎬 
Get ready to be spellbound as TeleGenAIsis transports you to a realm where imagination knows no bounds. 🌌🌈 
Join us on this extraordinary journey where technology and magic collide in perfect harmony. 🚀🎥 Let the adventure begin! ✨🔥</i></b>""", unsafe_allow_html=True)

login(users)

st.info("Want to create a new account? Sign up!")
if st.button('Sign up'):
    switch_page('Signup')