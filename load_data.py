import pandas as pd

# Load MovieLens data
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', usecols=[0, 1], names=['movie_id', 'title'])
print("Ratings sample:")
print(ratings.head())
print("\nMovies sample:")
print(movies.head())