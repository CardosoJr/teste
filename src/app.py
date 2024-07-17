import plotly.express as px
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from pathlib import Path
import streamlit as st

df = pd.read_csv(Path("./Data/turnover.csv"))

fig = px.histogram(df, x = 'RendaMensal', color = 'Turnover')

st.title("Nosso primeiro dashboard")
st.plotly_chart(fig)
