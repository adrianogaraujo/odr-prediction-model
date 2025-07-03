import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="ODR Dashboard", layout="wide")

st.title("📊 Dashboard de Disputas - Plataforma ODR")

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv("../data/odr_disputas_simuladas.csv")

df = load_data()

# Seções
st.sidebar.header("Filtros")
tipo_disputa = st.sidebar.multiselect("Tipo de Disputa", df["tipo_disputa"].unique(), default=df["tipo_disputa"].unique())
perfil_usuario = st.sidebar.multiselect("Perfil do Usuário", df["perfil_usuario"].unique(), default=df["perfil_usuario"].unique())

# Filtro aplicado
df_filtered = df[df["tipo_disputa"].isin(tipo_disputa) & df["perfil_usuario"].isin(perfil_usuario)]

st.subheader("Resumo Geral")
col1, col2, col3 = st.columns(3)
col1.metric("Disputas Filtradas", len(df_filtered))
col2.metric("Taxa de Acordo", f"{df_filtered['resultado_final'].mean() * 100:.1f}%")
col3.metric("Valor Médio Reclamado", f"R$ {df_filtered['valor_reclamado'].mean():,.2f}")

st.divider()

st.subheader("Distribuição por Tipo de Disputa")
fig, ax = plt.subplots()
sns.countplot(data=df_filtered, x="tipo_disputa", hue="resultado_final", palette="Set2", ax=ax)
ax.set_title("Acordos vs Não Acordos por Tipo")
ax.set_xlabel("Tipo de Disputa")
ax.set_ylabel("Contagem")
st.pyplot(fig)

st.divider()

st.subheader("Correlação entre Variáveis Numéricas")
corr = df_filtered.select_dtypes(include=["float64", "int64"]).corr()
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)
