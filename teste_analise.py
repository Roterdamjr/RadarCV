
from google import genai
from funcoes_ai_pdf import fn_busca_job, fn_busca_resumo, fn_busca_opniao, fn_gerar_score
from funcoes import fn_busca_conteudo_curriculo
import os
from dotenv import load_dotenv

arq_curriculo = 'curriculos/CV Pedro Argento.pdf'

load_dotenv()
client = genai.Client(api_key=os.getenv("API_KEY"))

print('========================================================')
prompt = fn_busca_resumo(arq_curriculo)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[prompt])

for chunk in response:
    print(chunk.text, end="")
 
print('========================================================')
prompt = fn_busca_opniao(fn_busca_conteudo_curriculo(arq_curriculo), fn_busca_job())

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[prompt])

for chunk in response:
    print(chunk.text, end="")

print('========================================================')
prompt = fn_gerar_score(fn_busca_conteudo_curriculo(arq_curriculo),fn_busca_job())

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=[prompt])

for chunk in response:
    print(chunk.text, end="")