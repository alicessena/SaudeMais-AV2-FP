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

def buscar_por_crm(lista, crm_busca):
    for profissional in lista:
        partesCrm = profissional["crm"].strip().split() #tira espaços e quebra o CRM em 2
        if len(partesCrm) == 2: #se CRM for na estrutura [CRM-SP, 234123] 
            regiaoCrm, numero = partesCrm #regiao vira CRM-SP e numero vira 234123
            if numero == crm_busca:
                return profissional
    return None

def gerar_novo_id(lista):
    if not lista:
        return 1
    return max(item['id'] for item in lista) + 1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')