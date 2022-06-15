import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph, src, dest):
    inf = sys.maxsize #retorna o valor infinito
    node_data = {"esc1" : {"cost" : inf, "pred" : []},
    "int4" : {"cost": inf, "pred": []},
    "int5" : {"cost": inf, "pred": []},
    "int6" : {"cost": inf, "pred": []},
    "int7" : {"cost": inf, "pred": []},
    "esc3" : {"cost": inf, "pred": []},
    "int8" : {"cost": inf, "pred": []},
    "int2" : {"cost": inf, "pred": []},
    "int1" : {"cost": inf, "pred": []},
    "int3" : {"cost": inf, "pred": []},
    "desc1": {"cost": inf, "pred": []},
    "int9" : {"cost": inf, "pred": []},
    "int10": {"cost": inf, "pred": []},
    "desc2": {"cost": inf, "pred": []},
    "int11": {"cost": inf, "pred": []},
    "esc2" : {"cost": inf, "pred": []},
    "int13": {"cost": inf, "pred": []},
    "int12": {"cost": inf, "pred": []},
    "desc3": {"cost": inf, "pred": []}
    }
    node_data[src]["cost"] = 0
    visited = []
    temp = src
    for i in range(18):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                cost = node_data[temp]["cost"] + graph[temp][j] # calcula o custo do nó
                if cost < node_data[j]["cost"]:
                    node_data[j]["cost"] = cost # montagem do custo
                    node_data[j]["pred"] = node_data[temp]["pred"] + list(temp) # montagem do Path
                heappush(min_heap, (node_data[j]["cost"], j))
        heapify(min_heap) # função para criar o heap minimo certo
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]["cost"]))    
    print("Shortest Path: " + node_data[dest]["pred"] + list(dest))


if __name__ == "__main__":
    graph = {"esc1" : {"int4" : 200},
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

    source = "int2"
    destination = "desc3"
    dijsktra(graph, source, destination)