# aplicação FastAPI

from fastapi import FastAPI
from src.api_service import RecommendationService

# instancia FastAPI
app = FastAPI(title="Sistema de recomendação - API", version="1.0")

# instancia o serviço de recomendação
service = RecommendationService()


@app.get("/")
def root():
    return {"message": "API de Recomendação Online"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int, n: int=5):
    """
        Retorna recomendações personalizadas para o usuario informado.
        Exemplo: /recommend/10?n=5
    """

    result = service.get_user_recommendations(user_id, n)
    return result

