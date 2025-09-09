

# ---------- a) Intervalo em vetor ordenado ----------

def intervalo_vetor_ordenado(vetor):
    
    menor = vetor[0]
    maior = vetor[-1]
    return maior - menor


# ---------- b) Intervalo em vetor desordenado ----------

def intervalo_vetor_desordenado(vetor):
    
    menor = vetor[0]
    maior = vetor[0]

    for elem in vetor[1:]:
        if elem < menor:
            menor = elem
        elif elem > maior:
            maior = elem

    return maior - menor


# EXEMPLOS DE USO

if __name__ == "__main__":

    # a) Vetor ordenado
    print("a) Intervalo em vetor ordenado")
    vetor_ordenado = [1, 3, 5, 7, 9, 12]
    print("Vetor ordenado:", vetor_ordenado)
    print("Intervalo:", intervalo_vetor_ordenado(vetor_ordenado))  # 12 - 1 = 11

    # b) Vetor desordenado
    print("\nb) Intervalo em vetor desordenado")
    vetor_desordenado = [7, 2, 10, 4, 8, 3]
    print("Vetor desordenado:", vetor_desordenado)
    print("Intervalo:", intervalo_vetor_desordenado(vetor_desordenado))  # 10 - 2 = 8
