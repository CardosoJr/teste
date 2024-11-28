import pandas as pd
from pathlib import Path
import src.funcoes as f
import plotly_express as px
import streamlit as st

df = pd.read_csv(Path("data/turnover.csv"))
df = f.dropna(df, "Idade")
df = f.remove_outliers(df, 'RendaMensal')

st.title("Análise de Turnover")
fig = px.histogram(df, x = "RendaMensal")
st.plotly_chart(fig)