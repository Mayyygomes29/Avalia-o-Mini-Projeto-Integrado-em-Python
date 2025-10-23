import os
import numpy as np
import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Analisando arquivo .json')

response = requests.get("http://127.0.0.1:8000/stats")

if response.status_code == 200:
    data = response.json()
    st.subheader("Dados completos")
    st.json(data)

    if "números pares de qtd" in data:
        st.subheader("Números pares de quantidade")
        pares_df = pd.DataFrame(data["números pares de qtd"], columns=["quantidade"])
        st.write(pares_df)

    if "números elevado ao quadrado de qtd" in data:
        st.subheader("Números elevados ao quadrado")
        quadrado_df = pd.DataFrame(data["números elevado ao quadrado de qtd"], columns=["faixas"])
        st.write(quadrado_df)

    if "RESUMO" in data:
        st.subheader("Estatísticas Resumo")
        resumo_df = pd.DataFrame(data["RESUMO"]).T 
        st.write(resumo_df)

    st.subheader("Histograma")
    reading = pd.read_csv('C:/Users/55219/Downloads/pós/python 2/trab final/data/vendas.csv',sep=";", encoding="utf-8")
    fig, ax = plt.subplots()
    ax.hist(x=reading['quantidade'], bins=20)
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('Frequência')
    st.pyplot(fig)

    contagem = reading['categoria'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(contagem.values,labels=contagem.index,autopct='%1.1f%%',startangle=90, radius=3, center=(4, 4), 
           wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
    ax.set_title("Distribuição por Categoria")
    st.pyplot(fig)

else:
    st.error(" Não foi possível conectar à API")
