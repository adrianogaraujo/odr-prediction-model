from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carregamento do modelo (deve ser treinado e salvo previamente com joblib)
# model = joblib.load("modelo_odr.pkl")

@app.route("/")
def home():
    return "API de Previsão de Acordo ODR ativa."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        # prediction = model.predict_proba(df)[0][1]
        prediction = 0.78  # Simulação fixa
        return jsonify({"probabilidade_de_acordo": round(prediction, 2)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
