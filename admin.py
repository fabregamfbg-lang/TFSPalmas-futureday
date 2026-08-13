# admin.py - rode local: streamlit run admin.py
import streamlit as st
import pandas as pd

df = pd.read_csv("respostas_future_day.csv")
st.title("📊 Admin Future Day")
st.metric("Total", len(df))
st.dataframe(df)
st.download_button("Baixar CSV", df.to_csv(index=False).encode(), "inscricoes.csv")
