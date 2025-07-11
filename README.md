# Movie Recommendation System

A personalized movie recommendation system built using collaborative filtering with the MovieLens 100K dataset. This project leverages machine learning (SVD) to recommend movies based on user ratings, served via a Flask API. A Streamlit interface (in progress) allows users to input preferences and view recommendations. The project demonstrates skills in machine learning, web development, and API design, optimized for scalability and user experience.

## Features
- **Collaborative Filtering**: Uses Singular Value Decomposition (SVD) to generate movie recommendations based on user similarity.
- **Flask API**: Provides a REST endpoint (`/recommend`) to serve recommendations for a given user ID.
- **Streamlit UI** (planned): Interactive web interface for users to input preferences and view recommendations.
- **Dataset**: MovieLens 100K, containing 100,000 ratings from 943 users across 1,682 movies.

## Tech Stack
- **Python**: Core programming language.
- **Scikit-learn**: For SVD-based collaborative filtering.
- **Pandas/NumPy**: Data processing and matrix operations.
- **Flask**: Lightweight REST API.
- **Streamlit** (planned): Web-based user interface.
- **Git**: Version control and GitHub hosting.

## Setup
### Prerequisites
- Python 3.8 or later
- Git
- MovieLens 100K dataset ([download here](https://grouplens.org/datasets/movielens/))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommender.git
   cd movie-recommender
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install scikit-learn pandas numpy flask streamlit
   ```
4. Download and unzip the MovieLens 100K dataset into the `ml-100k` folder:
   ```bash
   unzip ml-100k.zip
   ```

## Usage
1. **Run the Flask API**:
   ```bash
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5000`.

2. **Test the API**:
   - In a browser, visit: `http://127.0.0.1:5000/recommend?user_id=1`
   - Example response:
     ```json
     {
       "user_id": 1,
       "recommendations": [
         "Star Wars (1977)",
         "Fargo (1996)",
         "Return of the Jedi (1983)",
         "Toy Story (1995)",
         "Raiders of the Lost Ark (1981)"
       ]
     }
     ```

3. **Run the Streamlit UI** (planned for Day 2):
   ```bash
   streamlit run ui.py
   ```
   Access the UI at `http://127.0.0.1:8501` to input a user ID (1–943) and view recommendations.

## Project Structure
```
movie-recommender/
├── ml-100k/              # MovieLens dataset
├── app.py                # Flask API
├── train_model.py        # SVD model training
├── load_data.py          # Data loading and exploration
├── ui.py                 # Streamlit UI (planned)
├── README.md             # Project documentation
```

