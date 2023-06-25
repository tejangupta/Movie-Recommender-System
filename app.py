import streamlit as st
import sys
from src.utils import load_object, recommend
from src.exception import CustomException
from src.logger import logging

st.header('Movie Recommender System Using Machine Learning')

try:
    # Load movie list
    logging.info('Loading movie list...')
    movies = load_object('artifacts/movie_list.pkl')
    movie_list = movies['title'].values
    logging.info('Movie list loaded successfully.')

    # Select a movie
    selected_movie = st.selectbox('Type or select a movie from the dropdown', movie_list)

    if st.button('Show Recommendation'):
        logging.info(f"Recommendation requested for movie: '{selected_movie}'")

        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        # Display recommended movies
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

        # Log successful recommendation
        logging.info(f"Recommended movies for '{selected_movie}' displayed successfully.")
except Exception as e:
    logging.error(f'An error occurred: {str(e)}')
    raise CustomException(e, sys)
