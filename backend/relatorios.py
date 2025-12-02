from flask import Blueprint, jsonify
from utils import carregar_arquivo
import os

bp_relatorios = Blueprint('relatorios', __name__)
ARQUIVO_CONSULTAS = os.path.join(os.path.dirname(__file__), 'dados', 'consultas.json')

@bp_relatorios.route('/relatorios/consultas/profissional', methods=['GET'])
def relatorio_consultas_profissional():
    try:
        consultas = carregar_arquivo(ARQUIVO_CONSULTAS)
        report = {}
        for c in consultas:
            prof_name = c.get('profissional', {}).get('nome', 'Desconhecido')
            if prof_name not in report:
                report[prof_name] = []
            report[prof_name].append(c)
        
        return jsonify(report), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp_relatorios.route('/relatorios/consultas/data', methods=['GET'])
def relatorio_consultas_data():
    try:
        consultas = carregar_arquivo(ARQUIVO_CONSULTAS)
        report = {}
        for c in consultas:
            date = c.get('data', 'Sem Data')
            if date not in report:
                report[date] = []
            report[date].append(c)
        
        return jsonify(report), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
