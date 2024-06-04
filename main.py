import streamlit as st

st.title("Hello World")

query = st.text_input("¿Cuál es tu consulta?")

st.markdown("### Tu consulta es: " + query)