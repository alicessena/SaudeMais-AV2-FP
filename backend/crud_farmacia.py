from flask import Blueprint, request, jsonify
from utils import carregar_arquivo, salvar_arquivo
import os

bp_farmacia = Blueprint('farmacia', __name__)
ARQUIVO = os.path.join(os.path.dirname(__file__), 'dados', 'medicamentos.json')

@bp_farmacia.route('/medicamentos', methods=['GET'])
def get_medicamentos():
    try:
        dados = carregar_arquivo(ARQUIVO)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_farmacia.route('/medicamentos', methods=['POST'])
def create_medicamento():
    try:
        novo = request.json
        if not novo.get('nome'):
            return jsonify({"error": "Nome is required"}), 400
        
        dados = carregar_arquivo(ARQUIVO)
        # Check duplicate by name (case insensitive)
        if any(m['nome'].lower() == novo['nome'].lower() for m in dados):
            return jsonify({"error": "Medicamento already exists"}), 409
            
        dados.append(novo)
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Medicamento created", "data": novo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_farmacia.route('/medicamentos/<nome>', methods=['PUT', 'PATCH'])
def update_medicamento(nome):
    try:
        patch = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        found = False
        for m in dados:
            if m['nome'].lower() == nome.lower():
                m.update(patch)
                found = True
                break
        
        if not found:
            return jsonify({"error": "Medicamento not found"}), 404
            
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Medicamento updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_farmacia.route('/medicamentos/<nome>', methods=['DELETE'])
def delete_medicamento(nome):
    try:
        dados = carregar_arquivo(ARQUIVO)
        dados = [m for m in dados if m['nome'].lower() != nome.lower()]
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Medicamento deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
