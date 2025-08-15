import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id)
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend_movies(movie):
    movie_index=movies_df[movies_df['title'] == movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movie_posters=[]
    for i in movie_list:
        movie_id=movies_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies, recommended_movie_posters
movies_list=pickle.load(open('movies_dict.pkl', 'rb'))
movies_df = pd.DataFrame(movies_list)
similarity= pickle.load(open('similarty.pkl', 'rb'))
st.title("Movie Recommendation System")
selected_movie = st.selectbox(
    'Which movie would you like to watch?',
    (movies_df['title'].values)
)
if st.button('Recommend'):
   recommended_movie_names,recommended_movie_posters = recommend_movies(selected_movie)
   col1, col2, col3, col4, col5 =  st.columns(5)
   with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
   with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])

   with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
   with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
        
   with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])