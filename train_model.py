from src.recommender_model import RecommenderModel
from src.recommerder_evaluator import RecommenderEvaluator
from src.recommender_utils import RecommenderUtils
import pandas as pd


def main():
    print("Iniciando treinamento e avaliação do modelo de recomendação...")

    # Instanciar Modelo
    model_handler = RecommenderModel()

    # Carregar dados
    data = model_handler.load_data("data/processed/user_ratings.csv")

    # Treinar Modelo
    trainset, testset = model_handler.train(data)

    # Avaliar Modelo

    evaluator = RecommenderEvaluator()
    rmse, mae = evaluator.evaluate(model_handler.model, testset)

    # salvar modelo treinado
    model_handler.save_model()

    # Gerando recomendações de exemplo
    print("\n Gerando recomendações para amostragem....")
    predictions = model_handler.model.test(testset)
    top_n = RecommenderUtils.get_top_n(predictions, n=5)

    movies_df = pd.read_csv("data/processed/user_ratings.csv")[['movie_id', 'title']].drop_duplicates()
    RecommenderUtils.show_user_recommendations(user_id=10, top_n=top_n, movies_df=movies_df)


if __name__ == "__main__":
    main()