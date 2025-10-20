import pandas as pd

class DataCleaner:
    @staticmethod
    def clean_movies(movies: pd.DataFrame) -> pd.DataFrame:
        movies = movies.copy()
        movies['title'] = movies['title'].str.strip()
        movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')

        

        print(f"Filmes Limpos: {movies.isnull().sum().sum()} Valores Nulos encontrados")
        return movies
    
    @staticmethod
    def clean_users(users: pd.DataFrame) -> pd.DataFrame:
        users = users.copy()
        users['occupation'] = users['occupation'].str.lower()
        print(f"Usuários Limpos: {users.isnull().sum().sum()} Valores nulos encontrados")
        return users
    
    @staticmethod
    def clean_ratings(ratings: pd.DataFrame) -> pd.DataFrame:
        ratings = ratings.copy()
        ratings.dropna(inplace=True)
        ratings['rating'] = ratings['rating'].astype(int)
        print(f"Avaliações Limpas: {ratings.shape}")
        return ratings
    