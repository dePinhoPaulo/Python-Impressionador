import streamlit as st
from data_loader import carregar_dados

base = carregar_dados()

def criar_card(icone, numero, texto, coluna_card):
    container = coluna_card.container(border=True)
    coluna_esquerda, coluna_direita = container.columns([1, 2.5])
    coluna_esquerda.image(f"imagens/{icone}")
    coluna_direita.write(numero)
    coluna_direita.write(texto)

coluna_esquerda, coluna_meio, coluna_direita = st.columns([1, 1, 1])

base_emandamento = base[base["Status"]=="Em andamento"]
base_fechados = base[base["Status"].isin(["Em andamento", "Finalizado"])]


criar_card("oportunidades.png", f'{base["Código Projeto"].count():,}', "Oportunidades", coluna_esquerda)
criar_card("projetos_fechados.png", f'{base_fechados["Código Projeto"].count():,}', "Projetos Fechados", coluna_meio)
criar_card("em_andamento.png", f'{base_emandamento["Código Projeto"].count():,}', "Em andamento", coluna_direita)

criar_card("total_orcado.png", f'R${base_fechados["Valor Orçado"].sum():,}', "Total Orçado", coluna_esquerda)
criar_card("total_pago.png", f'R${base_fechados["Valor Negociado"].sum():,}', "Total Pago", coluna_meio)
criar_card("desconto.png", f'R${base_fechados["Desconto Concedido"].sum():,}', "Total Desconto", coluna_direita)

st.table(base.head(15))