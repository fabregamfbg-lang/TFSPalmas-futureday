import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Admin Future Day", page_icon="📊", layout="wide")

st.title("📊 Admin - Pré-Inscrição Future Day")

try:
    df = pd.read_csv("respostas_future_day.csv")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de inscrições", len(df))
    col2.metric("Última inscrição", df.iloc[-1]["timestamp"] if len(df) > 0 else "—")
    col3.metric("Primeira inscrição", df.iloc[0]["timestamp"] if len(df) > 0 else "—")
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Baixar CSV completo", 
        csv, 
        f"inscricoes_future_day_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
        "text/csv",
        use_container_width=True
    )
    
except FileNotFoundError:
    st.warning("Arquivo `respostas_future_day.csv` não encontrado. Rode o app principal primeiro.")
