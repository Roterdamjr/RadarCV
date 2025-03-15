import fitz
from tinydb import TinyDB, Query
import tkinter as tk
from tkinter import filedialog
import os


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
 

def fn_consulta_curriculos():
  db = TinyDB('curriculos.json')
  return [item['nome'] for item in db.all() if 'nome' in item]

def fn_exclui_curriculos():
    db = TinyDB('curriculos.json')
    db.truncate()
 
def fn_inserir_analise(nome, resumo,diferenciais,nota):
    db = TinyDB('analises.json')
    analise = {
      'nome': nome,
      'resumo': resumo,
      'opniao': diferenciais,
      'nota': nota 
    }
    db.insert(analise)

