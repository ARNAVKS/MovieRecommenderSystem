#you can run this code only to run your movie recommender system, the thing you have to do is you have to add 'similarity.pkl' file and 'movies_2.csv' file in your project PyCharm workspace
#make sure you have installed streamlit and pandas in PyCharm through terminal

#importing the libraries
import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')
sim=pickle.load(open('similarity.pkl','rb'))
movies = pd.read_csv('movies_2.csv')

def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distance = sim[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

option=st.selectbox('Choose a movie', movies['title'].values)
if st.button('Recommend'):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
#now after writing this code open terminal and write 'streamlit run name_of_the_file.py' in the terminal and press enter to run the code
