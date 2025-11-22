import json
import os

ARQUIVO_DB = "banco_dados.json"

def carregar_banco():
    """Lê o arquivo JSON e retorna os dados. Se não existir, cria vazio."""
    if not os.path.exists(ARQUIVO_DB):
        dados_iniciais = {
            "pacientes": [],
            "profissionais": [],
            "consultas": [],
            "exames": [],
            "farmacia": []
        }
        salvar_banco(dados_iniciais)
        return dados_iniciais
    
    try:
        with open(ARQUIVO_DB, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Erro ao ler o banco de dados. Arquivo corrompido.")
        return {}

def salvar_banco(dados):
    """Escreve o dicionário de dados no arquivo JSON."""
    with open(ARQUIVO_DB, 'w', encoding='utf-8') as f:
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