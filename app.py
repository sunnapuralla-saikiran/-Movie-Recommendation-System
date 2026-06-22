import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read movie dataset
movies = pd.read_csv("movies.csv")

# Create similarity matrix
cv = CountVectorizer()
matrix = cv.fit_transform(movies['genre'])
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie_name):
    movie_name = movie_name.lower()

    for i in range(len(movies)):
        if movies.iloc[i]['title'].lower() == movie_name:

            scores = list(enumerate(similarity[i]))
            scores = sorted(scores, key=lambda x: x[1], reverse=True)

            recommendations = []

            for movie in scores[1:4]:
                recommendations.append(
                    movies.iloc[movie[0]]['title']
                )

            return recommendations

    return []

# Streamlit UI
st.title("🎬Movie Recommendation System")
st.write("Get movie recommendations based on your favorite movies.")

movie = st.selectbox(
    "Select a Movie",
    movies['title']
)

if st.button("Recommend"):

    result = recommend(movie)

    st.subheader("Recommended Movies")

    if result:
        for movie in result:
            st.write("⭐", movie)
    else:
        st.write("No recommendations found.")