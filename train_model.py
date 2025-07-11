import pandas as pd
from sklearn.decomposition import TruncatedSVD
import numpy as np

# Load data
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])

# Create user-item matrix
user_item_matrix = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

# Train SVD model
svd = TruncatedSVD(n_components=20, random_state=42)
matrix = svd.fit_transform(user_item_matrix)

# Compute correlation matrix for recommendations
corr_matrix = np.corrcoef(matrix)

# Function to get recommendations
def get_recommendations(user_id, user_item_matrix, corr_matrix, movies, top_n=5):
    user_idx = user_id - 1  # Adjust for 0-based indexing
    similar_users = corr_matrix[user_idx]
    similar_user_indices = similar_users.argsort()[-top_n-1:-1][::-1]
    recommended_movies = []
    for idx in similar_user_indices:
        rated_movies = user_item_matrix.iloc[idx][user_item_matrix.iloc[idx] > 0].index
        recommended_movies.extend(rated_movies)
    recommended_movies = list(set(recommended_movies))[:top_n]
    return movies[movies['movie_id'].isin(recommended_movies)]['title'].tolist()

# Example: Get recommendations for user ID 1
movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', usecols=[0, 1], names=['movie_id', 'title'])
recommendations = get_recommendations(1, user_item_matrix, corr_matrix, movies)
print("Recommendations for user 1:", recommendations)