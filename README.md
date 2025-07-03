# odr-prediction-model
🔍 Previsão de Acordos em Sistemas de Resolução de Conflitos Online (ODR) com Machine Learning
odr-prediction-model/
├── data/
│ └── odr_disputas_simuladas.csv # Base de dados fictícia
├── notebooks/
│ ├── 01_exploratory_analysis.ipynb # Análise exploratória
│ ├── 02_model_training.ipynb # Treinamento de modelos
│ └── 03_fairness_analysis.ipynb # Análise de justiça algorítmica
├── src/
│ ├── preprocessing.py # Limpeza e engenharia de atributos
│ └── model.py # Treinamento e avaliação dos modelos
├── app/
│ └── api_flask.py # Protótipo de API para predição (opcional)
│ └── dashboard_streamlit.py # Dashboard interativo (opcional)
├── requirements.txt # Dependências
└── README.md # Descrição do projeto

# 🔍 ODR Agreement Prediction – Previsão de Acordos em Plataformas de Resolução de Conflitos Online

Este projeto simula e analisa um sistema de previsão de acordos judiciais em plataformas ODR (Online Dispute Resolution), com foco em eficiência, justiça algorítmica e aplicação de modelos supervisionados de machine learning. A proposta é fornecer inteligência preditiva a mediadores e operadores de plataformas digitais, auxiliando na resolução de disputas de forma rápida, justa e com menor custo.

---

## 📌 Objetivo

Desenvolver um pipeline de ciência de dados capaz de prever, com base em informações iniciais de uma disputa, a probabilidade de que ela seja resolvida por meio de acordo. O projeto também contempla a avaliação de **justiça algorítmica** (fairness), contribuindo com discussões sobre ética em sistemas automatizados.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Pandas, NumPy, Scikit-learn
- Matplotlib / Seaborn / Plotly
- Jupyter Notebook
- AIF360 (para fairness)
- Flask (para simulação de API, opcional)
- Power BI ou Streamlit (para visualização interativa)

---

## 🗂️ Estrutura do Projeto

