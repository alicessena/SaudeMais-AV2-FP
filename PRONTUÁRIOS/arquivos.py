import json
import os

ARQUIVO = 'prontuarios.json'

def carregar_dados():
    """Carrega os prontuários do arquivo JSON"""
    try:
        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return dados if isinstance(dados, list) else []
        return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def salvar_dados(prontuario):
    """Salva os prontuários em arquivo JSON"""
    try:
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            json.dump(prontuario, f, indent=4, ensure_ascii=False)
        print(" Dados salvos com sucesso!")
    except Exception as e:
        print(f" Erro ao salvar dados: {e}")