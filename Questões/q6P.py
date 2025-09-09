def busca_profundidade_iterativa(matriz_adj, s):
    n = len(matriz_adj)
    visitado = [0] * n
    pred = [-1] * n
    pilha = [s]
    visitado[s] = 1

    while pilha:
        u = pilha[-1]  # consulta topo
        encontrou = False

        for v in range(n):
            if matriz_adj[u][v] == 1 and visitado[v] == 0:
                visitado[v] = 1
                pred[v] = u
                pilha.append(v)
                encontrou = True
                break  # desce no primeiro vizinho não visitado

        if not encontrou:
            pilha.pop()

    return visitado, pred
