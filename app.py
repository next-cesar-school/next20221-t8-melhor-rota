
import sqlite3
from flask import Flask, render_template, request, jsonify
import json
import caminhoes_controller
import init_db
import grafo_new


app = Flask(__name__)



@app.route('/caminhoes', methods=["GET"])
def get_caminhoes():
    lista_caminhoes = caminhoes_controller.get_caminhoes()    
    
    return jsonify(lista_caminhoes)
    
@app.route("/caminhao", methods=["POST"])
def insert_caminhao():
    caminhao_details = request.get_json()
    descricao = caminhao_details["descricao"]
    localizacao = caminhao_details["localizacao"]
    status = caminhao_details["status"]
    result = caminhoes_controller.insert_caminhao(descricao, localizacao, status)
    return jsonify(result)

@app.route("/caminhao/<id>", methods=["PUT"])
def update_caminhao(id):
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
    
    id = f'Id: {caminhao[0]}'
    descricao = f'Caminhão: {caminhao[1]}'
    localizacao = f'Localização: {caminhao[2]}'
        
    if caminhao[3] == "True":
        status = "Caminhão está cheio, seguir para área de Descarregamento mais próxima!!!" 
        lista_rotas = grafo_new.find_all_paths(grafo_new.mapa, caminhao[2], 'desc1')
        menor_desc1 = grafo_new.menor_rota(lista_rotas)
        lista_rotas = grafo_new.find_all_paths(grafo_new.mapa, caminhao[2], 'desc2')
        menor_desc2 = grafo_new.menor_rota(lista_rotas)
        lista_rotas = grafo_new.find_all_paths(grafo_new.mapa, caminhao[2], 'desc3')
        menor_desc3 = grafo_new.menor_rota(lista_rotas)
        if menor_desc1 < menor_desc2 and menor_desc1 < menor_desc3:
            retorna_menor = menor_desc1
        elif menor_desc2 < menor_desc1 and menor_desc2 < menor_desc3:
            retorna_menor = menor_desc2
        else:
            retorna_menor = menor_desc3    
    else:
        status = "Caminhão está vazio, seguir para escavadeira mais próxima!!!"
        lista_rotas = grafo_new.find_all_paths(grafo_new.mapa, caminhao[2], 'esc1')
        menor_esc1 = grafo_new.menor_rota(lista_rotas)
        lista_rotas = grafo_new.find_all_paths(grafo_new.mapa, caminhao[2], 'esc2')
        menor_esc2 = grafo_new.menor_rota(lista_rotas)
        lista_rotas = grafo_new.find_all_paths(grafo_new.mapa, caminhao[2], 'esc3')
        menor_esc3 = grafo_new.menor_rota(lista_rotas) 
        if menor_esc1 < menor_esc2 and menor_esc1 < menor_esc3:
            retorna_menor = menor_esc1
        elif menor_esc2 < menor_esc1 and menor_esc2 < menor_esc3:
            retorna_menor = menor_esc2
        else:
            retorna_menor = menor_esc3            
#    return jsonify(caminhao, status)
    return jsonify(id, descricao, localizacao, status, retorna_menor)


if __name__ == "__main__":
 #   init_db.create_tables()
    app.run()