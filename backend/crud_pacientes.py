from flask import Blueprint, request, jsonify
from utils import carregar_arquivo, salvar_arquivo
import os

bp_pacientes = Blueprint('pacientes', __name__)
ARQUIVO = os.path.join(os.path.dirname(__file__), 'dados', 'pacientes.json')

@bp_pacientes.route('/pacientes', methods=['GET'])
def get_pacientes():
    try:
        dados = carregar_arquivo(ARQUIVO)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_pacientes.route('/pacientes', methods=['POST'])
def create_paciente():
    try:
        novo = request.json
        if not novo.get('cpf') or not novo.get('nome'):
            return jsonify({"error": "CPF and Nome are required"}), 400
        
        dados = carregar_arquivo(ARQUIVO)
        # Check duplicate
        if any(p['cpf'] == novo['cpf'] for p in dados):
            return jsonify({"error": "Paciente already exists"}), 409
            
        dados.append(novo)
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Paciente created", "data": novo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_pacientes.route('/pacientes/<cpf>', methods=['PUT', 'PATCH'])
def update_paciente(cpf):
    try:
        patch = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        found = False
        for p in dados:
            if p['cpf'] == cpf:
                p.update(patch)
                found = True
                break
        
        if not found:
            return jsonify({"error": "Paciente not found"}), 404
            
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Paciente updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_pacientes.route('/pacientes/<cpf>', methods=['DELETE'])
def delete_paciente(cpf):
    try:
        dados = carregar_arquivo(ARQUIVO)
        dados = [p for p in dados if p['cpf'] != cpf]
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Paciente deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
