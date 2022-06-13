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
        "int2" : {"int8": 260, "int1": 270, "int3": 250},
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
#mapa = {"esc1" : [("int4", 200)],
#        "int4" : [("esc1", 200), ("int5", 200)],
#        "int5" : [("int4", 200), ("int6", 100)],
#        "int6" : [("int5", 100), ("int7", 120)],
#        "int7" : [("int6", 120), ("esc3", 190), ("int8", 210), ("int13", 260)],
#        "esc3" : [("int7", 190)],
#        "int8" : [("int7", 210), ("int2", 260), ("int9", 250)],
#        "int2" : [("int8", 260), ("int1", 270), ("int3", 250)],
#        "int1" : [("int2", 270), ("int3", 200), ("desc1", 100)],
#        "int3" : [("int2", 250), ("int4", 120)],
#        "desc1": [("int1", 100)],
#        "int9" : [("int10", 130), ("int13", 90), ("int11", 130)],
#        "int10": [("int9", 130), ("desc2", 140)],
#        "desc2": [("int10", 140)],
#        "int11": [("int9", 130), ("esc2", 160)],
#        "esc2" : [("int11", 160)],
#        "int13": [("int7", 260), ("int9", 90), ("int12", 300)],
#        "int12": [("int13", 300), ("int11", 170), ("desc3", 190)],
#        "desc3": [("int12", 190)]
#        }
class heapmin(dict):
    def __init__(self):
        self.__heap = []
        dict.__init__(self)

    def menor(self):
#        if len(self) == 0:
#            raise IndexError, "Dicionario Vazio"
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            ultimoItem = heap.pop()
            pontoInsercao = 0
#            smallChild = 0           
            while 1:
                smallChild = 2*(pontoInsercao+1)
                print(smallChild)
                print(len(heap))
                print(smallChild+1)

                if smallChild+1 < len(heap) and heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or ultimoItem <= heap[smallChild]:
                    heap[pontoInsercao] = ultimoItem
                    break
                heap[pontoInsercao] = heap[smallChild]
                
        return heap[0][1]        
    def __iter__(self):
        def iterfn():
            while len(self) > 0:
                x = self.menor()
                yield x
                del self[x]
        return iterfn()

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        heap =  self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.heap.sort()
        else:
            newPair = (val,key)   
            pontoInsercao = len(heap)
            heap.append(None)
            while pontoInsercao > 0 and newPair < heap[(pontoInsercao-1)//2]:
                heap[pontoInsercao] = heap[(pontoInsercao-1)//2]
                pontoInsercao = (pontoInsercao-1)//2
            heap[pontoInsercao] = newPair
    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
        return self[key]    


class grafo:
    
    def Dijkstra(G, start, end=None):
        D = {}
        P = {}
        Q = heapmin()
        Q[start] = 0

        for v in Q:
            D[v] = Q[v]
            if v == end: break

            for w in G[v]:
                vwLenght = D[v] + G[v][w]
                if w in D:
                    if vwLenght < D[w]:
                        raise ValueError
                elif w not in Q or vwLenght < Q[w]:
                    Q[w] = vwLenght    
                    P[w] = v
        return (D,P)            

    def shortestPath(G, start, end):
        D,P = grafo.Dijkstra(G, start, end)
        Path = []
        while 1:
            Path.append(end)
            if end == start: break
            end = P[end]
        Path.reverse()    
        return Path

print(grafo.shortestPath(mapa, 'int1', 'desc1'))
