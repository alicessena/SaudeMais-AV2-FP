from flask import Blueprint, request, jsonify
from utils import carregar_arquivo, salvar_arquivo
import os
import time

bp_consultas = Blueprint('consultas', __name__)
ARQUIVO = os.path.join(os.path.dirname(__file__), 'dados', 'consultas.json')

@bp_consultas.route('/consultas', methods=['GET'])
def get_consultas():
    try:
        dados = carregar_arquivo(ARQUIVO)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_consultas.route('/consultas', methods=['POST'])
def create_consulta():
    try:
        novo = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        # Generate ID
        novo['id'] = str(int(time.time() * 1000))
        
        dados.append(novo)
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Consulta created", "name": novo['id'], "data": novo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_consultas.route('/consultas/<id>', methods=['PUT', 'PATCH'])
def update_consulta(id):
    try:
        patch = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        found = False
        for c in dados:
            if str(c.get('id')) == str(id):
                c.update(patch)
                found = True
                break
        
        if not found:
            return jsonify({"error": "Consulta not found"}), 404
            
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Consulta updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_consultas.route('/consultas/<id>', methods=['DELETE'])
def delete_consulta(id):
    try:
        dados = carregar_arquivo(ARQUIVO)
        dados = [c for c in dados if str(c.get('id')) != str(id)]
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Consulta deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
