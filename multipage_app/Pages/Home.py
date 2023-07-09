import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle
from streamlit_extras.switch_page_button import switch_page
# from Pages.QA import on_click_callback
# from Pages.Signup import sign_up
import vertexai
from vertexai.language_models import TextGenerationModel
import os
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from streamlit_extras.let_it_rain import rain
import random

st.set_page_config(
    page_title = "TeleGenAIsis",
    page_icon = "🤖",
)
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/924824/pexels-photo-924824.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.markdown("<h1 style='text-align: center;'>TeleGenAIsis🤖</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Future of entertainment!!🎥</h2>", unsafe_allow_html=True)

# st.markdown("""<b><i>If you want recomendations from our Generative AI model click "GenAI" button below. 
#          Else you can search the movie of your choice and get recommendations based on similarity here!</i></b>""", unsafe_allow_html=True)
# if st.button('GenAI'):
#     switch_page('qa')

st.sidebar.success("Select a page above.")

emoji_lst = ["🎈", "🥳", "🎉","🍿", "🎥", "🎬", "📺", "🍩", "🥤", "🍫", "🎞️", "🎧", "🍕", "🎮", "🎙️", "🔥", "🎉", "🎊"]
random_emo = random.choice(emoji_lst)

rain(
    emoji=random_emo,
    font_size=40,  # the size of emoji
    falling_speed=3,  # speed of raining
    animation_length=1,  # for how much time the animation will happen
)

df=pickle.load(open('movie_list.pkl','rb'))
similarity_score=pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie_user):
    movie_index = df[df.title == movie_user].index.values[0]

    similar_movies = pd.DataFrame(enumerate(similarity_score[movie_index])).drop(0, axis='columns').sort_values(by=1, ascending=False)
    similar_movies['Names'] = list(map(lambda x: str(np.squeeze(df[df.index == x]['title'].values)), similar_movies.index.values))
    similar_movies['id'] = list(map(lambda x: int(np.squeeze(df[df.index == x]['id'].values)), similar_movies.index.values))

    recommended_movie_posters = []
    for i in range(13):
        id=similar_movies.id.values[i]
        # Fetch movie poster from the TMDB Database
        recommended_movie_posters.append(fetch_poster(id))

    return similar_movies.Names.values[:13],recommended_movie_posters


with open(r'C:\Users\vishwebh\Desktop\Teleco\multipage_app\Pages\username.txt', 'r') as file:
    prompt_1 = file.readlines()


def why_this():
    vertexai.init(project="gen-telegenaisis", location="us-central1")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
    response = model.predict(
        """
        Now, consider you have suggested some movies to this person, whose demographics are given below. Describe in 
        only three lines as to why you have recommended the movies to the user. Keep the read interesting to the user
        with emojies and lingo targeting their demographics!
        Strictly do not include movie names in the paragraph.
        
        Example: (If you are recommending movies to a 24yr old, male, engineer)
        Hi! These are the recommended films for young engineers like you! They showcase the power of innovation, problem-solving, 
        and the pursuit of knowledge, inspiring you to think outside the box and push your boundaries. 
        These movies will entertain and motivate you to aspire for greatness in your engineering journey!

        """+str(prompt_1),
        **parameters
    )
    return f'{response.text}'


def recommend_gen():
    with open(r"C:\Users\vishwebh\Desktop\Teleco\multipage_app\Pages\temp_file.txt", 'r') as mov_file:
        movie_names = mov_file.readlines()
    
    movie_names = [name.strip() for name in movie_names]
    recommend_movie_posters = []
    valid_movie_names = []
    for my_movie in movie_names:
        print(my_movie)
        movie_df = df[df.title == my_movie]

        if not movie_df.empty:
            movie_index = movie_df.index.values[0]
            movie_id = df.loc[movie_index, 'id']
            recommend_movie_posters.append(fetch_poster(movie_id))
            valid_movie_names.append(my_movie)
    
    with open(r"C:\Users\vishwebh\Desktop\Teleco\multipage_app\Pages\temp_file.txt", "w") as emp_file:
        emp_file.write("")

    return valid_movie_names, recommend_movie_posters

# selected_movie = st.text_input('Enter movie name:')

# selected_movie = st.selectbox(
# 'Search a movie you want to watch here:',
# (list(df.title.values)))

# Semantic search
selected_movie = st.text_input('Enter anything!')
if selected_movie:
    vertexai.init(project="gen-telegenaisis", location="us-central1")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
    response = model.predict(
        """
        You are a movie recommender, the user can type anything!
        Your response must not include any extra words other than
        a list containing 4 - 12 movies only! Generated by you based on the above information. 
        
        The output should be of the form:

        List = ["movie1", "movie2", "movie 3"... So on, "movie11", "movie12"]

        Please return the list of movie titles as a string, properly formatted with double quotes around each title. 
        Ensure that any apostrophes within the titles are properly escaped with a backslash (\).
        
        User:
        """+selected_movie,
        **parameters
    )
    mov_str1 = f'{response.text}'
    print(mov_str1)
    if  mov_str1.startswith("List = ["):
        strt_idx = mov_str1.index('[')
        end_idx = mov_str1.index(']')
        list_ = mov_str1[strt_idx:end_idx+1]
        mov_list = eval(list_)
        with open("pages/temp_file.txt", "w") as file:
            for movie in mov_list:
                file.write(movie + "\n")

        names,poster = recommend_gen()
        col1, col2, col3, col4 = st.columns(4)
        for i in range(1,len(names)):
            try:
                if ( i % 4 == 1) and i < len(names):
                    with col1:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
                elif (i % 4 == 2):
                    with col2:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
                elif (i % 4 == 3):
                    with col3:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
                elif (i % 4 == 0):
                    with col4:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
            except IndexError:
                break

else:
    text_1 = """
    You are a Movie recommender. You need to recommend movies based on the following demographics information of user.

    Example: 
    If the user demographics information is - age: 24, occupation: Engineer, gender: Male

    Your recommendation will be something like this - 

    Hi! These are the recommended films for young engineers like you! They showcase the power of innovation, problem-solving, 
    and the pursuit of knowledge, inspiring you to think outside the box and push your boundaries. 
    These movies will entertain and motivate you to aspire for greatness in your engineering journey!

    User demographics information:
    """

    text_2 = """
    Important instructions to follow (Strictly follow these instruction):

    Your response must not include any extra words other than
    a list containing 4 - 12 movies only! Generated by you based on the above information. 
    The output should be of the form:

    List = ["movie1", "movie2", "movie 3"... So on, "movie11", "movie12"]

    Please return the list of movie titles as a string, properly formatted with double quotes around each title. 
    Ensure that any apostrophes within the titles are properly escaped with a backslash (\).

    """

    vertexai.init(project="gen-telegenaisis", location="us-central1")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
    response = model.predict(
        text_1+str(prompt_1)+text_2,
        **parameters
    )
    # st.write(f"Response from Model: {response.text}")
    # st.write(f'{response.text}')

    mov_str = f'{response.text}' # string type
    # mov_str = repr(mov_str)
    if  mov_str.startswith("List = ["):
        strt_idx = mov_str.index('[')
        end_idx = mov_str.index(']')
        list_ = mov_str[strt_idx:end_idx+1]
        mov_list = eval(list_)
        with open("pages/temp_file.txt", "w") as file:
            for movie in mov_list:
                file.write(movie + "\n")

        # if st.button('Show Recommendation'):
        #     names,poster = recommend(selected_movie)
        #     col1, col2, col3, col4 = st.columns(4)
        #     for i in range(1,len(names)):
        #         if ( i % 4 == 1):
        #             with col1:
        #                 st.text(names[i])
        #                 st.image(poster[i])
        #                 if st.button('See More/Less'):
        #                     vertexai.init(project="gen-telegenaisis", location="us-central1")
        #                     parameters = {
        #                         "temperature": 0.2,
        #                         "max_output_tokens": 256,
        #                         "top_p": 0.8,
        #                         "top_k": 40
        #                     }
        #                     model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
        #                     response = model.predict(
        #                         text_1+str(prompt_1)+text_2,
        #                         **parameters
        #                     )
        #                     st.markdown(f'<div style="text-align: justify;">{response.text}</div>', unsafe_allow_html=True)

        #         elif (i % 4 == 2):
        #             with col2:
        #                 st.text(names[i])
        #                 st.image(poster[i])
        #         elif (i % 4 == 3):
        #             with col3:
        #                 st.text(names[i])
        #                 st.image(poster[i])
        #         elif (i % 4 == 0):
        #             with col4:
        #                 st.text(names[i])
        #                 st.image(poster[i])
        # else:
        descr = why_this()
        st.markdown(f'<b><i>{descr}</i></b>', unsafe_allow_html=True)
                
        names,poster = recommend_gen()
        col1, col2, col3, col4 = st.columns(4)
        for i in range(1,len(names)):
            try:
                if ( i % 4 == 1):
                    with col1:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
                elif (i % 4 == 2):
                    with col2:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
                elif (i % 4 == 3):
                    with col3:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
                elif (i % 4 == 0):
                    with col4:
                        st.text(names[i])
                        st.image(poster[i])
                        vertexai.init(project="gen-telegenaisis", location="us-central1")
                        parameters = {
                            "temperature": 0.2,
                            "max_output_tokens": 256,
                            "top_p": 0.8,
                            "top_k": 40
                        }
                        model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
                        response = model.predict(
                            """
                            Give a very short and interesting read of 3 lines only 
                            about this movie also make this description strictly personalized 
                            for the users demographics given below after the movie name:
                            
                            """+"name of movie: "+names[i]+" user demographics: "+str(prompt_1),
                            **parameters
                        )
                        stoggle("See More/Less",
                            f'{response.text}'
                        )
            except IndexError:
                break
    else:
        st.write("The AI model did not generate text stating with 'List = '")

    


    





 


# text = """
# You are a good movie finder/ movie Identifier and know everything about movies accurately! 
# You can tell the name of the movie, given the dialogue or the name of any song from the movie.

# The following user input can be related to any of the Indian language or English movie. 
# It could be a song or dialogue or directly the movie name. 
# Give only the movie name do not give any more text in the result. 

# Recommend movies based on the below user demographics -

# User demographics:
# """

# User_Input = st.text_input("Enter anything you remember about any movie...")
# if User_Input:
#     vertexai.init(project="gen-telegenaisis", location="us-central1")
#     parameters = {
#         "temperature": 0.2,
#         "max_output_tokens": 256,
#         "top_p": 0.8,
#         "top_k": 40
#     }
#     model = TextGenerationModel.from_pretrained("text-bison") #text-bison@001
#     response = model.predict(
#         text+f"""{User_Input}""",
#         **parameters
#     )
#     st.write(f"Response from Model: {response.text}")

# if st.button('Show Recommendation'):
#     names,poster = recommend(selected_movie)
#     col1, col2, col3, col4 = st.columns(4)
#     for i in range(1,len(names)):
#         if ( i % 4 == 1):
#             with col1:
#                 st.text(names[i])
#                 st.image(poster[i])
#         elif (i % 4 == 2):
#             with col2:
#                 st.text(names[i])
#                 st.image(poster[i])
#         elif (i % 4 == 3):
#             with col3:
#                 st.text(names[i])
#                 st.image(poster[i])
#         elif (i % 4 == 0):
#             with col4:
#                 st.text(names[i])
#                 st.image(poster[i])

# elif st.button('Personalize'):
#     names,poster = recommend_gen()
#     col1, col2, col3, col4 = st.columns(4)
#     for i in range(1,len(names)):
#         if ( i % 4 == 1):
#             with col1:
#                 st.text(names[i])
#                 st.image(poster[i])
#         elif (i % 4 == 2):
#             with col2:
#                 st.text(names[i])
#                 st.image(poster[i])
#         elif (i % 4 == 3):
#             with col3:
#                 st.text(names[i])
#                 st.image(poster[i])
#         elif (i % 4 == 0):
#             with col4:
#                 st.text(names[i])
#                 st.image(poster[i])

