import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pickle
from pathlib import Path


class RecommenderModel:
    def __init__(self):
        self.model = None

    def load_data(self, path: str = "data/processed/user_ratings.csv"):
        df = pd.read_csv(path)
        reader = Reader(rating_scale=(1,5))
        data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)
        print(f"Dados carregados para treinamento: {df.shape}")
        return data
    
    def train(self, data):
        print("Iniciando treinamento do modelo SVD")
        trainset, testset = train_test_split(data, test_size=0.2)
        self.model = SVD(n_factors=100, n_epochs=25, lr_all=0.005, reg_all=0.02)
        self.model.fit(trainset)
        print("Treinamento Concluído")
        return trainset, testset
    
    def save_model(self, path: str = "models/recommender_svd.pkl"):
        Path("models").mkdir(exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self.model, f)
        print(f"Modelo salvo em: {path}")