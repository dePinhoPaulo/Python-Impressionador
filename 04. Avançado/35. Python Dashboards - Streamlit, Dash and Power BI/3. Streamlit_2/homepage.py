import streamlit as st


# containers
# columns

coluna_esquerda, coluna_direita = st.columns([1, 1.5])

coluna_esquerda.title("Hash&Co")
coluna_esquerda.write("#### Bem vindo, Fulano") # markdown
botao_dashboards = coluna_esquerda.button("Dashboard Projetos")
botao_indicadores = coluna_esquerda.button("Principais Indicadores")

if botao_dashboards:
    st.switch_page("dashboard.py")
if botao_indicadores:
    st.switch_page("indicadores.py")

container = coluna_direita.container(border=True)
container.image("imagens/time-comunidade.webp")