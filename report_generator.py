import requests
import os
import docker

def generate_report():
    response = requests.get("https://api-inference.huggingface.co/models")
    models = response.json()

    # Extract the top 10 downloaded models
    top_10_models = sorted(models, key=lambda x: x['downloads'], reverse=True)[:10]

    # Print the top 10 models
    for i, model in enumerate(top_10_models, 1):
        print(f"{i}. Model: {model['model_name']}, Downloads: {model['downloads']}")

    # Stop the container
    client = docker.from_env()
    container_id = os.getenv('HOSTNAME')
    client.containers.get(container_id).stop()

if __name__ == "__main__":
    generate_report()
