from funcoes import fn_busca_nomes_analisados_db,fn_busca_analise_por_nome,fn_busca_nota_final
import streamlit as st


st.title("Análise de Nomes")

# Busca os nomes analisados do banco de dados
nomes_analisados = fn_busca_nomes_analisados_db()
  

#notas = [fn_busca_nota_final(nome) for nome in nomes_analisados]

# Widget de seleção para o usuário escolher um nome
nome_selecionado = st.selectbox("Selecione um nome analisado:", nomes_analisados)

if nome_selecionado:
    st.subheader(f"Informações de: {nome_selecionado}")

    # Busca os dados de análise do nome selecionado
    dados_analise = fn_busca_analise_por_nome(nome_selecionado)

    if dados_analise:
        # Exibe o resumo em uma textarea
        resumo = dados_analise.get("resumo", "Resumo não disponível.")
        st.subheader("Resumo:")
        st.text_area("Resumo", resumo, height=200, disabled=True)

        # Textarea para a opinião
        opiniao_inicial = dados_analise.get("opiniao", "")
        st.subheader("Opinião:")
        opiniao = st.text_area("Sua opinião sobre:", opiniao_inicial, height=200)

        # Textarea para a nota
        nota_inicial = dados_analise.get("nota", "")
        st.subheader("Nota:")
        nota = st.text_area("Sua nota:", nota_inicial, height=200)

    else:
        st.warning(f"Nenhum dado de análise encontrado para o nome: {nome_selecionado}")