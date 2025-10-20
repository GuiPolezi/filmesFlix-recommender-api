import pandas as pd
import pickle
from surprise import SVD
from src.recommender_utils import RecommenderUtils

class RecommendationService:
    def __init__(self, model_path="models/recommender_svd.pkl", data_path="data/processed/user_ratings.csv"):
        # carregar modelos e dados
        with open(model_path, "rb") as f:
            self.model: SVD = pickle.load(f)
        self.data = pd.read_csv(data_path)
        self.movies = self.data[['movie_id', 'title']].drop_duplicates()
        print(" Modelo e dados carregados no serviço de recomendação ")

    def get_user_recommendations(self, user_id: int, n: int= 5):
        # Verifica se o usuário existe
        if user_id not in self.data['user_id'].unique():
            return {"error": f"Usuário {user_id} não encontrado."}
        
        # Pega todos os filmes
        all_movies = self.movies['movie_id'].unique()

        # Pega filmes ja assistidos
        watched = self.data[self.data['user_id'] == user_id]['movie_id'].unique()

        # Gera previsões para filmes não assistidos
        predictions = [
            (mid, self.model.predict(user_id, mid).est)
            for mid in all_movies if mid not in watched
        ]

        # Ordena pelas maiores notas previstas
        top_n = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]

        # Monta a resposta Legível
        recommendations = []
        for movie_id, score in top_n:
            title = self.movies.loc[self.movies['movie_id'] == movie_id, 'title'].values
            recommendations.append({
                "movie_id": int(movie_id),
                "title": title[0] if len(title) > 0 else str(movie_id),
                "predicted_rating": round(score, 2)
            })
    
        return {
            "user_id": user_id,
            "recommendations": recommendations
        }
    

