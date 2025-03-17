import streamlit as st
import asyncio
from dotenv import load_dotenv
from google import genai
from funcoes_ai_db import fn_busca_resumo, fn_busca_curriculo_db, fn_busca_job,fn_busca_opiniao,fn_gerar_score
from funcoes import fn_inserir_analise_db,fn_exclui_analise_db, fn_busca_candidatos
import os



def fn_gera_response(prompt):
    client = genai.Client(api_key=os.getenv("API_KEY"))

    response_text = ""
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=[prompt]
    )

    for chunk in response:
        response_text += chunk.text 
    return response_text


st.title("Análise de Currículos")

load_dotenv()

fn_exclui_analise_db()

if st.button("Analisar"):
 
    for nome_candidato in fn_busca_candidatos():
       # nome_candidato = 'Bart'
        st.write(f"Analisando candidato: **{nome_candidato}**")
        curriculo = fn_busca_curriculo_db(nome_candidato)

        with st.status("Gerando resumo..."):
            prompt = fn_busca_resumo(curriculo)
            resumo = fn_gera_response(prompt)
            if resumo:  # Only proceed if resumo was generated successfully
                st.write("Resumo:", resumo)

        with st.status("Gerando opinião..."):
            prompt = fn_busca_opiniao(curriculo, fn_busca_job())
            opiniao = fn_gera_response(prompt)
            if opiniao:  
                st.write("Opiniao:", opiniao)

        with st.status("Calculando nota..."):
            prompt = fn_gerar_score(curriculo, fn_busca_job())
            nota = fn_gera_response(prompt)
            if nota:  
                st.write("Nota:", nota)
    
        fn_inserir_analise_db(nome_candidato, resumo,opiniao,nota)

st.write('Pronto!')