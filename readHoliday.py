import openpyxl
import streamlit as st

wb = openpyxl.load_workbook(‘feriadosNacionais.xlsx’)
sheet = wb[‘Feriados’]

C1 = sheet['C1'] # read direct value in cell C1

st.write (C1.value)
