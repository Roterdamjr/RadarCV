import streamlit as st
import asyncio
from dotenv import load_dotenv
from google import genai
from funcoes_ai_db import fn_busca_resumo, fn_busca_curriculo_db, fn_busca_job,fn_busca_opiniao,fn_gerar_score
from funcoes import fn_inserir_analise_db,fn_exclui_analises_db,  fn_busca_curriculos_db,fn_exclui_analise_db, fn_busca_nomes_analisados_db
import os 



st.title("Análise de Currículos")


nome_candidato='Bart'



st.write(f"Analisando candidato: **{nome_candidato}**")
curriculo = fn_busca_curriculo_db(nome_candidato)


with st.status("Gerando resumo..."):
    prompt = fn_busca_resumo(curriculo)
    print('**************************************************************************************')
    print(prompt)


with st.status("Gerando opinião..."):
    prompt = fn_busca_opiniao(curriculo, fn_busca_job())
    print('**************************************************************************************')
    print(prompt)


with st.status("Calculando nota..."):
    prompt = fn_gerar_score(curriculo, fn_busca_job())
    print('**************************************************************************************')
    print(prompt)



st.write('Pronto!')


