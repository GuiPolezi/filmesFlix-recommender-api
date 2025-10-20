import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, data_dir: str = 'data/raw'):
        self.data_dir = Path(data_dir)

    def load_movies(self) -> pd.DataFrame:
        movie_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + [f'genre_{i}' for i in range(19)]
        movies_path = self.data_dir / "u.item"
        movies = pd.read_csv(movies_path, sep='|', encoding='latin-1', names=movie_cols)
        print(f"Filmes carregados: {movies.shape}")
        return movies
    
    def load_ratings(self) -> pd.DataFrame:
        rating_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
        ratings_path = self.data_dir / "u.data"
        ratings = pd.read_csv(ratings_path, sep='\t', names=rating_cols)
        print(f"Avaliações Carregadas: {ratings.shape}")
        return ratings
    
    def load_users(self) -> pd.DataFrame:
        user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
        users_path = self.data_dir / "u.user"
        users = pd.read_csv(users_path, sep='|', names=user_cols)
        print(f"Usuários carregados: {users.shape}")
        return users
    
    