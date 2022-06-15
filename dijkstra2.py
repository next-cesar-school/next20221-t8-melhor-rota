import heapq
import sys

def alterar_prioridade(w, D):
    for i in range(len(D)):
        if D[i][1] == w:
            pos = i
            break
    D[pos] = (L[w], w)
    heapq._siftdown(D, 0, pos)

    return

n, m = map(int,input().split()) # ler numero de verices e arestas
n_out = [[] * n for i in range(n)] #define a lista de adjacencias
custo= [] #custos das arestas
infty = sys.maxsize #retorna o valor infinito
#definir matriz de custos (pesos)
for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(0)
        else:
            linha.append(infty)    
    custo.append(linha)        

for j in range(m):              #ler as arestas do digrafo
    a, b, c = map(int, input().split())   #ler aresta de a para b com custo c
    n_out[a].append(b)                    # b é vizinho de saida de a
    custo[a][b] = c

#inicializadores

marca = n*[0]
L = n*[infty]
raiz = 0 # no caso do mapa é o ponto de partida
L[raiz] = 0 #0 na raiz do algoritimo
D = [(0, raiz)]
for w in range(0,n):
    if w != raiz:
        heapq.heappush(D, L[w])




