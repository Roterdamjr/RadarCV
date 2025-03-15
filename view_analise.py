import streamlit as st
import asyncio
from dotenv import load_dotenv
from google import genai
from funcoes_ai_db import fn_busca_resumo, fn_busca_curriculo_db, fn_busca_job,fn_busca_opniao,fn_gerar_score
import os

st.title("Análise de Currículos")

load_dotenv()

try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

client = genai.Client(api_key=os.getenv("API_KEY"))

##################### Resumo ######################
curriculo = fn_busca_curriculo_db('bert')
prompt = fn_busca_resumo(curriculo)

response_text = ""
response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[prompt]
)

for chunk in response:
    response_text += chunk.text 

st.text_area("Resumo", value=response_text, height=300)

##################### Opniao ######################

prompt = fn_busca_opniao(curriculo, fn_busca_job())

response_text = ""
response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[prompt]
)

for chunk in response:
    response_text += chunk.text 

st.text_area("Opniao", value=response_text, height=300)

##################### score ######################

prompt = fn_gerar_score(curriculo, fn_busca_job())

response_text = ""
response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[prompt]
)

for chunk in response:
    response_text += chunk.text 

st.text_area("Score", value=response_text, height=300)