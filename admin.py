# admin.py - rode local: streamlit run admin.py
import streamlit as st
import pandas as pd

#df = pd.read_csv("respostas_future_day.csv")
#st.title("📊 Admin Future Day")
#st.metric("Total", len(df))
#st.dataframe(df)
#st.download_button("Baixar CSV", df.to_csv(index=False).encode(), "inscricoes.csv")

    df = pd.read_csv("respostas_future_day.csv")
except FileNotFoundError:
    st.error("CSV file not found")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("CSV file is empty")
    st.stop()

@st.cache_data
def load_data():
    return pd.read_csv("respostas_future_day.csv")

df = load_data()

search_term = st.text_input("🔍 Search in data")
if search_term:
    df = df[df.astype(str).apply(lambda x: x.str.contains(search_term, case=False)).any(axis=1)]

col1, col2, col3 = st.columns(3)
col1.metric("Total Responses", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Last Updated", pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"))

st.set_page_config(page_title="Admin Future Day", page_icon="📊", layout="wide")

columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
st.dataframe(df[columns], use_container_width=True)

# admin.py - rode local: streamlit run admin.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Admin Future Day", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("respostas_future_day.csv")
    except FileNotFoundError:
        st.error("❌ CSV file not found: respostas_future_day.csv")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading data: {str(e)}")
        st.stop()

df = load_data()

st.title("📊 Admin Future Day")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Responses", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Last Updated", pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"))

# Search functionality
search_term = st.text_input("🔍 Search in data")
if search_term:
    df = df[df.astype(str).apply(lambda x: x.str.contains(search_term, case=False)).any(axis=1)]
    st.info(f"Found {len(df)} matching records")

# Column selector
columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
st.dataframe(df[columns], use_container_width=True)

# Download button
st.download_button(
    label="📥 Baixar CSV",
    data=df.to_csv(index=False).encode(),
    file_name="inscricoes.csv",
    mime="text/csv"
)
