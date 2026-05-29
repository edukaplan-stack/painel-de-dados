# painel.py
import streamlit as st
import pandas as pd

st.title("Painel de Dados")
arquivo = st.file_uploader("Carregue uma tabela (.csv ou .xlsx)")
if arquivo:
    df = pd.read_csv(arquivo) if arquivo.name.endswith(".csv") else pd.read_excel(arquivo)
    st.dataframe(df)
    st.write(df.describe())
