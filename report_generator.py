import requests

def generate_report():
    response = requests.get("https://api-inference.huggingface.co/models")
    models = response.json()

    # Extract the top 10 downloaded models
    top_10_models = sorted(models, key=lambda x: x['downloads'], reverse=True)[:10]

    # Print the top 10 models
    for i, model in enumerate(top_10_models, 1):
        print(f"{i}. Model: {model['model_name']}, Downloads: {model['downloads']}")

if __name__ == "__main__":
    generate_report()
