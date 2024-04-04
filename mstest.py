import streamlit as st 
import pandas as pd
from msprogram import *

st.write("""
    # Mass Spectral Database
    """)
df = dataframecreator("./terp.txt")
st.write(df)