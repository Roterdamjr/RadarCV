import streamlit as st
import asyncio
from dotenv import load_dotenv
from google import genai
from funcoes_ai_db import fn_busca_resumo, fn_busca_curriculo_db, fn_busca_job,fn_busca_opniao,fn_gerar_score
from funcoes import fn_inserir_analise_db,fn_exclui_analise_db
import os

def fn_gera_response(prompt):
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

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

client = genai.Client(api_key=os.getenv("API_KEY"))

if st.button("Analisar"):
    nome_candidato ='Bart'

    ##################### Resumo ######################
    curriculo = fn_busca_curriculo_db(nome_candidato)
    prompt = fn_busca_resumo(curriculo)
    resumo = fn_gera_response(prompt)
    st.text_area("Resumo", value=fn_gera_response(prompt), height=300)
    #st.write('Gerando resumo!')
    ##################### Opniao ######################
    prompt = fn_busca_opniao(curriculo, fn_busca_job())
    opniao = fn_gera_response(prompt)
    st.text_area("Opniao", value=fn_gera_response(prompt), height=300)
   # st.write('Gerando opnião!')
    ##################### score ######################
    prompt = fn_gerar_score(curriculo, fn_busca_job())
    nota = fn_gera_response(prompt)
    st.text_area("Score", value=fn_gera_response(prompt), height=300)
    #st.write('Gerando Nota!')

    fn_exclui_analise_db()
   # fn_inserir_analise_db(nome_candidato, resumo,opniao,nota)

    st.write('Pronto!')