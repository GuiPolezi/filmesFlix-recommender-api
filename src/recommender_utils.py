import pandas as pd

class RecommenderUtils:
    @staticmethod
    def get_top_n(predictions, n=5):
        """Retorna os N melhores filmes recomendados por usuário"""
        from collections import defaultdict
        top_n = defaultdict(list)
        for uid, iid, true_r, est, _ in predictions:
            top_n[uid].append((iid, est))
        for uid, user_ratings in top_n.items():
            user_ratings.sort(key=lambda x: x[1], reverse=True)
            top_n[uid] = user_ratings[:n]
        return top_n
    
    @staticmethod
    def show_user_recommendations(user_id, top_n, movies_df):
        """Exibe recomendações legiveis"""
        if user_id not in top_n:
            print(f"Nenhuma recomendação encontrada para o usuário {user_id}")
            return
        
        print(f"\n Recomendações para o usuário {user_id}:")
        for movie_id, score in top_n[user_id]:
            title = movies_df.loc[movies_df['movie_id'] == movie_id, 'title'].values
            print(f" {title[0] if len(title) > 0 else movie_id} (Nota prevista: {score:.2f})")