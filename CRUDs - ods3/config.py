import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("ods-3---fp-firebase-adminsdk-fbsvc-692cba178f.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://ods-3---fp-default-rtdb.firebaseio.com/"
})

medicamentos_ref = db.reference("medicamentos")
pacientes_ref = db.reference("pacientes")
profissionais_ref = db.reference("profissionais")
exames_ref = db.reference("exames")
consultas_ref = db.reference("consultas")
prontuarios_ref = db.reference("prontuarios")

