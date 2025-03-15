import streamlit as st


st.title("Análise de Currículos")

if st.button("Analisar"):
    fn_exclui_curriculos()
    st.success("Currículos excluídos com sucesso!")

    st.session_state.clear()
    st.rerun()