from collections import deque

def busca_largura(matriz_adj, s):
    n = len(matriz_adj)           # número de vértices
    visitado = [0] * n
    pred = [-1] * n               # predecessores

    # inicialização
    visitado[s] = 1
    fila = deque([s])

    while fila:
        u = fila.popleft()
        for v in range(n):        # percorre todos os possíveis vizinhos
            if matriz_adj[u][v] == 1 and visitado[v] == 0:
                visitado[v] = 1
                pred[v] = u
                fila.append(v)

    return visitado, pred
