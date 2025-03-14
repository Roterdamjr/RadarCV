from funcoes import fn_insere_curriculo, fn_consulta_curriculos, fn_exclui_curriculos
import streamlit as st
import os

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

    st.session_state.clear()
    st.rerun()

st.header("Cadastro de Currículo")

# Inicializa os estados dos campos
if "nome_candidato" not in st.session_state:
    st.session_state["nome_candidato"] = ""

if "caminho_arquivo" not in st.session_state:
    st.session_state["caminho_arquivo"] = None

nome_candidato = st.text_input("Nome do candidato", key="nome_candidato")

file = st.file_uploader("Selecione um arquivo PDF", type=["pdf"])

if file is not None:
    file_path = os.path.join("uploads", file.name)
    os.makedirs("uploads", exist_ok=True)  # Criar diretório se não existir
    
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    st.session_state["caminho_arquivo"] = file_path

if st.session_state["caminho_arquivo"]:
    st.text(f"Arquivo selecionado: {st.session_state['caminho_arquivo']}")

if st.button("Salvar Currículo"):
    caminho_arquivo = st.session_state.get("caminho_arquivo", "")

    if nome_candidato and caminho_arquivo and os.path.exists(caminho_arquivo):
        resultado = fn_insere_curriculo(nome_candidato, caminho_arquivo)
        st.success(resultado)

        st.session_state.clear()
        st.rerun()
    else:
        st.error("Por favor, insira o nome do candidato e selecione um arquivo válido.")
