import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import json
import vertexai
from vertexai.language_models import TextGenerationModel

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/3374210/pexels-photo-3374210.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
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

def sign_up(users):
    st.title("Sign Up")
    first_nm = st.text_input('First Name')
    last_nm = st.text_input('Last Name') 
    age = st.text_input('Age')
    gender = st.text_input('Gender')
    occupation = st.text_input('Occupation')
    language = st.text_input('Language')
    location = st.text_input('Location')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    email = st.text_input("Email")
    genre = st.text_input("Which is your favourite genre?")
    str_exm = "likes "+genre+" movies"
    my_list_1 = [age, gender, occupation, str_exm]

    if st.button("Sign Up"):
        if password == confirm_password:
            if username in users:
                st.error("Username already exists. Please choose a different username.")
            else:
                # Store the user credentials in the dictionary
                users[username] = {"password": password, "email": email}
                with open("users.json", "w") as file:
                    json.dump(users, file)  # Save the updated users dictionary to the file
                st.success("Sign up successful. You can now log in.")
                with open(r'C:\Users\vishwebh\Desktop\Teleco\multipage_app\Pages\username.txt', 'w') as file:
                    for demo in my_list_1:
                        file.write(demo + "\n")
                
        else:
            st.error("Passwords do not match.")

st.markdown("<h1 style='text-align: center;'>TeleGenAIsis🤖</h1>", unsafe_allow_html=True)
st.markdown("""<b><i>Welcome to TeleGenAIsis! 🌟✨ Immerse yourself in a personalized OTT experience like never before. 
Our fusion of generative AI and telepathic wonders unlocks a world of enchantment. 🧙‍♀️🔮 Explore shows, movies, 
and documentaries tailored to your wildest dreams, with unexpected plot twists and mind-bending endings. 🌪️🎬 
Get ready to be spellbound as TeleGenAIsis transports you to a realm where imagination knows no bounds. 🌌🌈 
Join us on this extraordinary journey where technology and magic collide in perfect harmony. 🚀🎥 Let the adventure begin! ✨🔥</i></b>""", unsafe_allow_html=True)

sign_up(users)
st.info("Already have an account? Login now!")
if st.button('Login'):
    switch_page('Login')
