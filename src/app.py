import pandas as pd
from pathlib import Path
import streamlit as st
import plotly_express as px
from src import funcoes

df = pd.read_csv(Path("data/turnover.csv"))
df = funcoes.dropar_na(df, 'Idade', 0.05)
df = funcoes.limpar_outlier(df, 'RendaMensal')
df = funcoes.limpar_outlier(df, 'Idade')

st.title("Análise de Turnover")

fig = px.histogram(df, x = 'RendaMensal', color = 'Turnover')
st.plotly_chart(fig)
