
import asyncio
from dotenv import load_dotenv
from google import genai
from funcoes_ai_db import fn_busca_resumo, fn_busca_curriculo_db, fn_busca_job,fn_busca_opiniao,fn_gerar_score
from funcoes import fn_inserir_analise_db,fn_exclui_analises_db,  fn_busca_curriculos_db,fn_exclui_analise_db, fn_busca_nomes_analisados_db
import os 


nome_candidato='Bart'

curriculo = fn_busca_curriculo_db(nome_candidato)



prompt = fn_busca_resumo(curriculo)
with open('saida/01-resumo.txt', "w", encoding="utf-8") as arquivo:
    arquivo.write(prompt)

prompt = fn_busca_opiniao(curriculo, fn_busca_job())
with open('saida/02-opiniao.txt', "w", encoding="utf-8") as arquivo:
    arquivo.write(prompt)

prompt = fn_gerar_score(curriculo, fn_busca_job())
with open('saida/03-score.txt', "w", encoding="utf-8") as arquivo:
    arquivo.write(prompt)






