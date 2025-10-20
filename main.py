from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.data_merger import DataMerger
from src.utils import ensure_dirs
import pandas as pd


def main():
    print("Iniciando Pipeline de dados do sistema de recomendação...")
    ensure_dirs()

    #carregamento dos dados

    loader = DataLoader()
    movies = loader.load_movies()
    ratings = loader.load_ratings()
    users = loader.load_users()

    # Limpeza

    cleaner = DataCleaner()
    movies = cleaner.clean_movies(movies)
    ratings = cleaner.clean_ratings(ratings)
    users = cleaner.clean_users(users)

    # unificando

    merger = DataMerger()
    full_data = merger.merge_all(users, movies, ratings)

    # salvando dados processados
    processed_path = "data/processed/user_ratings.csv"
    full_data.to_csv(processed_path, index=False)
    print(f"Dados processados salvos em: {processed_path}")


if __name__ == "__main__":
    main()