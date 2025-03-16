from funcoes import fn_insere_curriculo, fn_consulta_curriculos, fn_exclui_curriculos
import streamlit as st
import os
import fitz  
from tinydb import TinyDB, Query
import shutil


def limpar_pasta_temp():
    try:
        shutil.rmtree("temp")  # Remove toda a pasta
        os.makedirs("temp", exist_ok=True)  # Recria a pasta vazia
    except Exception as e:
        st.error(f"Erro ao limpar a pasta temporária: {e}")

st.title("Cadastro de Currículos")

st.header("Currículos Cadastrados")

curriculos = fn_consulta_curriculos()
if curriculos:
    for curriculo in curriculos:
        st.write(curriculo)
else:
    st.write("Nenhum currículo cadastrado ainda.")

if st.button("Excluir"):
    fn_exclui_curriculos()
    st.success("Currículos excluídos com sucesso!")

 
st.header("Upload de Currículo")

nome_candidato = st.text_input("Nome do candidato", key="nome_candidato")

uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if uploaded_file is not None:
    file_path = os.path.join('temp', uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"Arquivo {uploaded_file.name} foi salvo")

if st.button("Gravar"):
    fn_insere_curriculo(nome_candidato ,file_path)
    limpar_pasta_temp()
    st.experimental_rerun()

