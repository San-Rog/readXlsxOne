import pandas as pd
import streamlit as st

with open('feriadosNacionais.pkl', 'rb') as file:
    model = pickle.load(file)
st.write(model)