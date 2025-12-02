from flask import Flask, jsonify
from flask_cors import CORS
import os
# Import Blueprints
from crud_pacientes import bp_pacientes
from crud_profissionais import bp_profissionais
from crud_farmacia import bp_farmacia
from crud_consultas import bp_consultas
from crud_exames import bp_exames
from crud_prontuarios import bp_prontuarios
from relatorios import bp_relatorios

# Initialize Data Directory
PASTA_DADOS = os.path.join(os.path.dirname(__file__), 'dados')
if not os.path.exists(PASTA_DADOS):
    os.makedirs(PASTA_DADOS)

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(bp_pacientes)
app.register_blueprint(bp_profissionais)
app.register_blueprint(bp_farmacia)
app.register_blueprint(bp_consultas)
app.register_blueprint(bp_exames)
app.register_blueprint(bp_prontuarios)
app.register_blueprint(bp_relatorios)

@app.route('/')
def health_check():
    return jsonify({"status": "ok", "message": "Hospital Sao Lucio Backend Running (Modular)"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
