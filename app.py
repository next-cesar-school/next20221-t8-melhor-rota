
import sqlite3
from flask import Flask, render_template, request, jsonify
import json
import caminhoes_controller
import init_db


app = Flask(__name__)



@app.route('/caminhoes', methods=["GET"])
def get_caminhoes():
    lista_caminhoes = caminhoes_controller.get_caminhoes()    
    print(lista_caminhoes)
    return jsonify(caminhoes=lista_caminhoes)
    
@app.route("/insert", methods=["POST"])
def insert_caminhao():
    caminhao_details = request.get_json()
    descricao = caminhao_details["descricao"]
    localizacao = caminhao_details["localizacao"]
    status = caminhao_details["status"]
    result = caminhoes_controller.insert_caminhao(descricao, localizacao, status)
    return jsonify(result)

@app.route("/alterar/<id>", methods=["PUT"])
def update_caminhao(id=0):
    caminhao_details = request.get_json()
    id = caminhao_details["id"]
    descricao = caminhao_details["descricao"]
    localizacao = caminhao_details["localizacao"]
    status = caminhao_details["status"]
    result = caminhoes_controller.update_caminhao(id, descricao, localizacao, status)
    return jsonify(result)

@app.route("/caminhao/<id>", methods=["DELETE"])
def delete_caminhao(id):
    result = caminhoes_controller.delete_caminhao(id)
    return jsonify(result)    


@app.route("/caminhao/<id>", methods=["GET"])
def get_caminhao_by_id(id):
    caminhao = caminhoes_controller.get_by_id(id)
    return jsonify(caminhao)  

if __name__ == "__main__":
 #   init_db.create_tables()
    app.run()