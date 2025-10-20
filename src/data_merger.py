import pandas as pd

class DataMerger:
    @staticmethod
    def merge_all(users: pd.DataFrame, movies: pd.DataFrame, ratings: pd.DataFrame) -> pd.DataFrame:
        df = ratings.merge(users, on='user_id', how='inner').merge(movies, on='movie_id', how='inner')
        print(f"Dados Mesclados: {df.shape}")
        return df