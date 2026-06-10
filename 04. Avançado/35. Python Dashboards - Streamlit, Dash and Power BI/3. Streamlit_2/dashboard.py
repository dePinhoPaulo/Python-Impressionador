import streamlit as st
from data_loader import carregar_dados
import plotly.express as px

base = carregar_dados()

coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 1, 1])

setor = coluna_esquerda.selectbox("Setor", list(base["Setor"].unique()))
status = coluna_meio.selectbox("Status", list(base["Status"].unique()))

base = base[(base["Setor"]==setor) & (base["Status"]==status)]
base_mensal = base.groupby(base["Data Chegada"].dt.to_period("M")).sum(numeric_only=True).reset_index()
base_mensal["Data Chegada"] = base_mensal["Data Chegada"].dt.to_timestamp()

container = st.container(border=True)
with container:
    # grafico de area
    st.write("### Total de Projetos por mês (R$)")
    grafico_area = px.area(base_mensal, x="Data Chegada", y="Valor Negociado")
    st.plotly_chart(grafico_area)


    # grafico de colunas
    st.table(base_mensal.head(15))