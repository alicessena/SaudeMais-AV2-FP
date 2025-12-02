from flask import Blueprint, request, jsonify
from utils import carregar_arquivo, salvar_arquivo
import os

bp_profissionais = Blueprint('profissionais', __name__)
ARQUIVO = os.path.join(os.path.dirname(__file__), 'dados', 'profissionais.json')

@bp_profissionais.route('/profissionais', methods=['GET'])
def get_profissionais():
    try:
        dados = carregar_arquivo(ARQUIVO)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_profissionais.route('/profissionais', methods=['POST'])
def create_profissional():
    try:
        novo = request.json
        if not novo.get('crm') or not novo.get('nome'):
            return jsonify({"error": "CRM and Nome are required"}), 400
        
        dados = carregar_arquivo(ARQUIVO)
        if any(p['crm'] == novo['crm'] for p in dados):
            return jsonify({"error": "Profissional already exists"}), 409
            
        dados.append(novo)
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Profissional created", "data": novo}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_profissionais.route('/profissionais/<crm>', methods=['PUT', 'PATCH'])
def update_profissional(crm):
    try:
        patch = request.json
        dados = carregar_arquivo(ARQUIVO)
        
        found = False
        for p in dados:
            if p['crm'] == crm:
                p.update(patch)
                found = True
                break
        
        if not found:
            return jsonify({"error": "Profissional not found"}), 404
            
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Profissional updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_profissionais.route('/profissionais/<crm>', methods=['DELETE'])
def delete_profissional(crm):
    try:
        dados = carregar_arquivo(ARQUIVO)
        dados = [p for p in dados if p['crm'] != crm]
        salvar_arquivo(ARQUIVO, dados)
        return jsonify({"message": "Profissional deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
