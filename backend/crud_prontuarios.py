from flask import Blueprint, request, jsonify
from utils import carregar_arquivo, salvar_arquivo
import os
import time

bp_prontuarios = Blueprint('prontuarios', __name__)
ARQUIVO = os.path.join(os.path.dirname(__file__), 'dados', 'prontuarios.json')

@bp_prontuarios.route('/prontuarios', methods=['GET'])
def get_prontuarios():
    try:
        dados = carregar_arquivo(ARQUIVO)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_prontuarios.route('/prontuarios', methods=['POST'])
def create_prontuario():
    try:
        novo = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        novo['id'] = str(int(time.time() * 1000))
        
        dados.append(novo)
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Prontuario created", "name": novo['id'], "data": novo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_prontuarios.route('/prontuarios/<id>', methods=['PUT', 'PATCH'])
def update_prontuario(id):
    try:
        patch = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        found = False
        for p in dados:
            if str(p.get('id')) == str(id):
                p.update(patch)
                found = True
                break
        
        if not found:
            return jsonify({"error": "Prontuario not found"}), 404
            
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Prontuario updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_prontuarios.route('/prontuarios/<id>', methods=['DELETE'])
def delete_prontuario(id):
    try:
        dados = carregar_arquivo(ARQUIVO)
        dados = [p for p in dados if str(p.get('id')) != str(id)]
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Prontuario deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
