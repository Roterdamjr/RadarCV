import fitz
from tinydb import TinyDB, Query
import tkinter as tk
from tkinter import filedialog
import os
import re 

def fn_busca_conteudo_curriculo(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()

    return text

def fn_insere_cargo( id, nome, prerequisitos, diferenciais, atividades):
    db = TinyDB('cargos.json')
    cargo = {
      'id': id,
      'nome': nome,
      'prerequisitos': prerequisitos,
      'diferenciais': diferenciais,
      'principais_atividades': atividades  # Corrigido o nome do campo
    }
    db.insert(cargo)

def fn_exclui_cargos():
    db = TinyDB('cargos.json')
    db.truncate()

def fn_consulta_cargos():

  db = TinyDB('cargos.json')
  Cargo = Query()
  resultados = db.search(Cargo.id.exists())  # Busca por qualquer cargo com um ID
  return resultados

def fn_insere_curriculo(nome_candidato, caminho_pdf):

    db = TinyDB('curriculos.json')
    
    text = ""
    with fitz.open(caminho_pdf) as doc:
        for page in doc:
            text += page.get_text()
    
    db.insert({'nome': nome_candidato,  'content': text})
 

def fn_busca_curriculos_db():
  db = TinyDB('curriculos.json')
  return [item['nome'] for item in db.all() if 'nome' in item]

def fn_exclui_curriculos_db():
    db = TinyDB('curriculos.json')
    db.truncate()

def fn_busca_candidatos_db():
    db = TinyDB('curriculos.json')
    return [item["nome"] for item in db.all()]

def fn_exclui_curriculo_db(nome_procurado):
    db = TinyDB('curriculos.json')
    Candidato = Query()
    resultados = db.search(Candidato.nome == nome_procurado)

    if resultados:
        db.remove(Candidato.nome == nome_procurado)
        db.close()
        return True
    else:
        db.close()
        return False

 
def fn_inserir_analise_db(nome, resumo,opiniao,nota):
    db = TinyDB('analises.json')
    analise = {
      'nome': nome,
      'resumo': resumo,
      'opiniao': opiniao,
      'nota': nota 
    }
    db.insert(analise)


def fn_busca_nomes_analisados_db():
    db = TinyDB('analises.json')
    return [item["nome"] for item in db.all()]

def fn_busca_analise_por_nome(nome):
    """Busca os dados de análise de um nome específico no banco de dados."""
    db = TinyDB('analises.json')
    Analise = Query()
    resultado = db.search(Analise.nome == nome)
    if resultado:
        return resultado[0]  # Retorna o primeiro resultado encontrado
    return None 


def fn_exclui_analises_db():
    db = TinyDB('analises.json')
    db.truncate()

def fn_exclui_analise_db(nome_procurado):
    db = TinyDB('analises.json')
    Analise = Query()
    resultados = db.search(Analise.nome == nome_procurado)

def fn_busca_nota_final(nome):
    db = TinyDB('analises.json')
    Analise = Query()
    result_raw = db.search(Analise.nome == nome)

    if not result_raw:
        print(f"Nenhuma análise encontrada para {nome}.")
        return None  # Or some other appropriate value to indicate no result

    # Access the first (and likely only) dictionary in the list
    first_result = result_raw[0]

    # Convert the relevant part of the dictionary to a string for regex
    result_text = str(first_result)

    pattern = r"(?i)Pontuação Final[:\s]*([\d,.]+(?:/\d{1,2})?)"
    match = re.search(pattern, result_text)

    if match:
        nota_final = match.group(1)
        #print(f"A pontuação final de {nome} é: {nota_final}")
    else:
        #print(f"Nenhuma pontuação final encontrada para {nome}.")
        nota_final = None  # Or some other appropriate value

    return nota_final



print(fn_busca_nota_final('Bart'))
