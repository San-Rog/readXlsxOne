import pandas as pd
import streamlit as st

df = pd.read_excel('feriadosNacionais.xlsx')
st.table(df)
