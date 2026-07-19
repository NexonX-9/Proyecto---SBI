import pyodbc
import pandas as pd
import streamlit as st

# Conexión aprovechando la autenticación mixta
def iniciar_conexion():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=proyecto_db;'
        'UID=sa;' # Tu usuario administrador de SQL
        'PWD=Password18.' 
    )
    return conn