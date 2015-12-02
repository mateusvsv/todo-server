from flask import Flask
from flask import render_template, jsonify, request
from flask.ext.cors import CORS
import json
from tarefa import Tarefa
from usuario import Usuario

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

USUARIOS = [
    Usuario(0, 'Mateus', []),
    Usuario(1, 'Fernando', []),
    Usuario(2, 'Batima', []),
]

TAREFAS = [
    Tarefa(0, 'Tarefa 0', USUARIOS[0].id, False),
    Tarefa(1, 'Tarefa 1', USUARIOS[1].id, True),
    Tarefa(2, 'Tarefa 2', USUARIOS[2].id, False),
]

@app.route('/tarefas')
def index():
    return render_template('index.html', tarefas=TAREFAS)

@app.route('/todos')
def get_tarefas():
    tarefas = tarefas_to_dict() 
    return jsonify(todos=tarefas) 

@app.route('/todos', methods=['POST',])
def cadastrar_tarefa():
    json = get_json()
    tarefa = Tarefa(len(TAREFAS), json.get('titulo'), json.get('usuario'))
    TAREFAS.append(tarefa)
    return jsonify(todo=tarefa.__dict__) 

@app.route('/todos/<int:id>', methods=['PUT',])
def editar_tarefa(id):
    json = get_json()
    TAREFAS[id] = Tarefa(id, json.get('titulo'), json.get('usuario'), json.get('completo'))
    return jsonify(TAREFAS[id].__dict__)

@app.route('/todos/<int:id>', methods=['DELETE',])
def excluir_tarefa(id):
    del TAREFAS[id];
    return ('', 204); 

@app.route('/usuarios')
def get_usuarios():
    usuarios = usuarios_to_dict()
    return jsonify(usuarios=usuarios)

def tarefas_to_dict():
    tarefas_dict = []
    for tarefa in TAREFAS:
        t = tarefa.__dict__
        tarefas_dict.append(t)
    return tarefas_dict

def usuarios_to_dict():
    usuarios_dict = []
    for usuario in USUARIOS:
        u = dict(id=usuario.id, nome=usuario.nome,todos=usuario.todos) 
        usuarios_dict.append(u)
    return usuarios_dict

def get_json():
    args = request.data
    params = json.loads(args)
    tarefa_json = params.get('todo')
    return tarefa_json 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
