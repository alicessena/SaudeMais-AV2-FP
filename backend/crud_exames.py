from flask import Blueprint, request, jsonify
from utils import carregar_arquivo, salvar_arquivo
import os
import time

bp_exames = Blueprint('exames', __name__)
ARQUIVO = os.path.join(os.path.dirname(__file__), 'dados', 'exames.json')

@bp_exames.route('/exames', methods=['GET'])
def get_exames():
    try:
        dados = carregar_arquivo(ARQUIVO)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_exames.route('/exames', methods=['POST'])
def create_exame():
    try:
        novo = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        novo['id'] = str(int(time.time() * 1000))
        
        dados.append(novo)
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Exame created", "name": novo['id'], "data": novo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_exames.route('/exames/<id>', methods=['PUT', 'PATCH'])
def update_exame(id):
    try:
        patch = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        found = False
        for e in dados:
            if str(e.get('id')) == str(id):
                e.update(patch)
                found = True
                break
        
        if not found:
            return jsonify({"error": "Exame not found"}), 404
            
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Exame updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_exames.route('/exames/<id>', methods=['DELETE'])
def delete_exame(id):
    try:
        dados = carregar_arquivo(ARQUIVO)
        dados = [e for e in dados if str(e.get('id')) != str(id)]
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Exame deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
