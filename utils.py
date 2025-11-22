# utils.py
import json
import os

def carregar_arquivo(nome_arquivo):
    """
    Lê um arquivo JSON específico e retorna a lista dentro dele.
    Se o arquivo não existir, retorna uma lista vazia.
    """
    if not os.path.exists(nome_arquivo):
        return []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {nome_arquivo} está corrompido.")
        return []

def salvar_arquivo(nome_arquivo, dados):
    """Salva uma lista de dados em um arquivo JSON específico."""
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def buscar_por_id(lista, id_busca):
    for item in lista:
        if item['id'] == id_busca:
            return item
    return None

def gerar_novo_id(lista):
    if not lista:
        return 1
    return max(item['id'] for item in lista) + 1