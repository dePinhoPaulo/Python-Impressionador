import pandas as pd
import streamlit as st
import joblib

# modelo = joblib.load('modelo.joblib')

# Transfomando variaveis do modelo em dicionarios
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Bed and breakfast', 'Condominium', 'Guest suite', 'Guesthouse', 'Hostel', 'House', 'Loft', 'Outros', 'Serviced apartment'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'],
            'cancelation_policy': ['flexible', 'moderate', 'strict', 'strict_14_with_grace_period']
            }

for item in x_numericos:
    valor  = st.number_input(f'{item}')

for item in x_tf:
    valor  = st.selectbox(f'{item}', ('Sim', 'Não'))
    
for item in x_listas:
    valor  = st.selectbox(f'{item}', x_listas[item])

botao = st.button('Prever Valor do Imovel')