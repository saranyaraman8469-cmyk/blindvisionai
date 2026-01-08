import mlflow
import random

mlflow.set_experiment("BlindVisionAI")

with mlflow.start_run():
    accuracy = random.uniform(0.7, 0.95)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_param("model", "ObstacleDetector")

    print("Logged accuracy:", accuracy)
