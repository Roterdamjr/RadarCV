import streamlit as st
import plotly.express as px
import pandas as pd

# (Seu código para buscar nomes e notas aqui)
def fn_busca_nomes_analisados_db():
    return ["Alice", "Bob", "Charlie", "David"]

def fn_busca_nota_final(nome):
    grades = {"Alice": 8.5, "Bob": 7.2, "Charlie": 9.0, "David": 6.8}
    return grades.get(nome, 0)

st.title("Ranking de Nomes por Nota (Plotly)")

nomes_analisados = fn_busca_nomes_analisados_db()
data = []
for nome in nomes_analisados:
    nota_final = fn_busca_nota_final(nome)
    data.append({"Nome": nome, "Nota Final": nota_final})

df = pd.DataFrame(data).sort_values(by="Nota Final", ascending=False)

# Criar o gráfico de barras com Plotly Express (uma interface de alto nível para Plotly)
fig = px.bar(df, x="Nome", y="Nota Final",
             title="Ranking de Nomes por Nota Final",
             labels={"Nota Final": "Nota Final", "Nome": "Nome"})
fig.update_layout(xaxis_tickangle=-45, xaxis_title="Nome", yaxis_title="Nota Final")

# Exibir o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)