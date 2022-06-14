import math



v = {"esc1", "esc2", "esc3", "desc1", "desc2", "desc3", "int1", "int2", "int3", "int4",
     "int5", "int6", "int7", "int8", "int9", "int10", "int11", "int12", "int3"}

mapa = {"esc1" : {"int4" : 200},
        "int4" : {"esc1": 200, "int5": 200},
        "int5" : {"int4": 200, "int6": 100},
        "int6" : {"int5": 100, "int7": 120},
        "int7" : {"int6": 120, "esc3": 190, "int8": 210, "int13": 260},
        "esc3" : {"int7": 190},
        "int8" : {"int7": 210, "int2": 260, "int9": 250},
        "int2" : {"int1": 270, "int3": 250, "int8": 260},
        "int1" : {"int2": 270, "int3": 200, "desc1": 100},
        "int3" : {"int2": 250, "int4": 120},
        "desc1": {"int1": 100},
        "int9" : {"int10": 130, "int13": 90, "int11": 130},
        "int10": {"int9": 130, "desc2": 140},
        "desc2": {"int10": 140},
        "int11": {"int9": 130, "esc2": 160},
        "esc2" : {"int11": 160},
        "int13": {"int7": 260, "int9": 90, "int12": 300},
        "int12": {"int13": 300, "int11": 170, "desc3": 190},
        "desc3": {"int12": 190}
        }

# monta uma lista com todas as rotas possivel do ponto1(start) para o ponto2(end)

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph[start]:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
'''
def menor_rota(lista_rotas):
    menor_ant = 9999999999999
    rota = []
    for i in range(len(lista_rotas)):
        menor = 0
        for z in range(len(lista_rotas[i])-1):
        
            lista_2 = lista_rotas[i]
            ponto1 = lista_2[z]

            if z+1 < len(lista_rotas[i]):
                ponto2 = lista_2[z+1]

            valor = mapa[ponto1][ponto2]
            menor = menor + valor

        if  menor < menor_ant:
            menor_ant = menor  
            rota = lista_rotas[i] 
    return menor, rota
caminhao = input("Informar o caminhão a ser utilizado: ")
if statusdocaminhao == True:
    lista_rotas = find_all_paths(mapa, posicaocaminhao, 'desc1')
    menor_desc1 = menor_rota(lista_rotas)
    lista_rotas = find_all_paths(mapa, posicaocaminhao, 'desc2')
    menor_desc2 = menor_rota(lista_rotas)
    lista_rotas = find_all_paths(mapa, posicaocaminhao, 'desc3')
    menor_desc2 = menor_rota(lista_rotas)
else:
    lista_rotas = find_all_paths(mapa, posicaocaminhao, 'esc1')
    menor_esc1 = menor_rota(lista_rotas)
    lista_rotas = find_all_paths(mapa, posicaocaminhao, 'esc2')
    menor_esc2 = menor_rota(lista_rotas)
    lista_rotas = find_all_paths(mapa, posicaocaminhao, 'esc3')
    menor_desc2 = menor_rota(lista_rotas)        
'''
# chamada da função para armazenagem das rotas
lista_rotas = find_all_paths(mapa, 'int5', 'esc1')

# rotina para pegar a menor rota com relação a sua distancia entre a soma dos pontos

menor_ant = 9999999999999
rota = []
for i in range(len(lista_rotas)):
    menor = 0
    for z in range(len(lista_rotas[i])-1):
        
        lista_2 = lista_rotas[i]
        ponto1 = lista_2[z]

        if z+1 < len(lista_rotas[i]):
            ponto2 = lista_2[z+1]

        valor = mapa[ponto1][ponto2]
        menor = menor + valor

    if  menor < menor_ant:
        menor_ant = menor  
        rota = lista_rotas[i] 

# Imprimi a menor distancia e a rota seguida

print(menor_ant)  
print(rota)