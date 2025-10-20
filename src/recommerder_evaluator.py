from surprise import accuracy

class RecommenderEvaluator:
    @staticmethod
    def evaluate(model, testset):
        print("Avaliando modelo...")
        predictions = model.test(testset)
        rmse = accuracy.rmse(predictions, verbose=True)
        mae = accuracy.mae(predictions, verbose=True)
        print(f"Avaliação concluída - RMSE: {rmse:.4f} | MAE: {mae:.4f}")
        return rmse, mae