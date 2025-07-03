import pandas as pd
from pathlib import Path
import plotly.express as px
import streamlit as st
import src.preprocessing as pp

df = pd.read_csv(Path("Data/turnover.csv"))

df = pp.remover_outliers(df, 'RendaMensal')

fig = px.histogram(df, x = 'RendaMensal')

st.title("Exemplo de App")
st.plotly_chart(fig)