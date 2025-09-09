

# ---------- a) Inserção na cabeça de uma lista ligada ----------

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def inserir_cabeca(self, valor):
        novo_no = No(valor)
        novo_no.prox = self.cabeca
        self.cabeca = novo_no

    def inserir_final(self, valor):
        """ b) Inserção no final de uma lista ligada (sem apontador de final) """
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = novo_no

    def exibir(self):
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.prox
        return elementos


# ---------- c) Encontrar o segundo menor elemento de um vetor ----------

def segundo_menor(vetor):
    if len(vetor) < 2:
        return None  # vetor inválido

    if vetor[0] < vetor[1]:
        menor, segundo = vetor[0], vetor[1]
    else:
        menor, segundo = vetor[1], vetor[0]

    for i in range(2, len(vetor)):
        if vetor[i] < menor:
            segundo = menor
            menor = vetor[i]
        elif vetor[i] < segundo and vetor[i] != menor:
            segundo = vetor[i]

    return segundo


# ---------- d) Somar duas matrizes quadradas de ordem n ----------

def somar_matrizes(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

    return C


# ---------- e) Contar ocorrências de um elemento em vetor desordenado ----------

def contar_ocorrencias(vetor, x):
    contador = 0
    for elem in vetor:
        if elem == x:
            contador += 1
    return contador



# EXEMPLOS DE USO

if __name__ == "__main__":

    # a) e b) Lista ligada
    print("a) e b) Lista Ligada")
    lista = ListaLigada()
    lista.inserir_cabeca(10)
    lista.inserir_cabeca(20)
    lista.inserir_final(30)
    lista.inserir_final(40)
    print("Elementos da lista:", lista.exibir())  # [20, 10, 30, 40]

    # c) Segundo menor elemento
    print("\nc) Segundo menor elemento")
    vetor = [7, 2, 9, 4, 1, 5]
    print("Vetor:", vetor)
    print("Segundo menor:", segundo_menor(vetor))  # 2

    # d) Soma de matrizes
    print("\nd) Soma de Matrizes")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("Matriz A:", A)
    print("Matriz B:", B)
    print("Soma A+B:", somar_matrizes(A, B))  # [[6, 8], [10, 12]]

    # e) Contar ocorrências
    print("\ne) Contar Ocorrências")
    vetor = [3, 1, 4, 3, 5, 3, 2]
    x = 3
    print("Vetor:", vetor)
    print(f"O elemento {x} ocorre", contar_ocorrencias(vetor, x), "vezes.")
