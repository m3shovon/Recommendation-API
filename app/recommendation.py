import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(user_preferences, movie_data):
    # Example recommendation logic
    similarities = cosine_similarity(user_preferences, movie_data)
    recommendations = np.argsort(similarities[0])[::-1]
    return recommendations
