import openpyxl
import streamlit as st

wb = openpyxl.load_workbook(‘feriadosNacionais.xlsx’)
sheet = wb['Feriados']
st.write (sheet)
