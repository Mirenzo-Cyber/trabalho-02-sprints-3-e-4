import time


# ==========================================
# 1. Bubble Sort O(n^2)
# ==========================================
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j]["id"] > lista[j + 1]["id"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return lista

# ==========================================
# 2. Selection Sort O(n^2)
# ==========================================
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]["id"] < lista[min_idx]["id"]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


# ==========================================
# 3. Insertion Sort O(n^2)
# ==========================================
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["id"] > chave["id"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


# ==========================================
# 4. Busca Binária O(log n)
# ==========================================
def busca_binaria_ativos(lista_ordenada, id_alvo):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio]["id"] == id_alvo:
            return meio
        elif lista_ordenada[meio]["id"] < id_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


# ==========================================
# 7. Aplicação Prática a uma Lista de Ativos de TI
# ==========================================
if __name__ == "__main__":
    ativos_ti = [
        {"id": "AT-042", "nome": "SRV-WEB-02"},
        {"id": "AT-005", "nome": "SRV-DB-PROD"},
        {"id": "AT-019", "nome": "SW-CORE-01"},
        {"id": "AT-001", "nome": "FW-BORDA-01"},
        {"id": "AT-023", "nome": "NB-SEC-04"}
    ]

    print("--- LISTA DESORDENADA ---")
    for a in ativos_ti:
        print(a)

    # Ordenando com Insertion Sort
    ativos_ordenados = insertion_sort(ativos_ti.copy())

    print("\n--- LISTA ORDENADA (Insertion Sort) ---")
    for a in ativos_ordenados:
        print(a)

    # Busca Binária do Ativo AT-019
    alvo = "AT-019"
    idx = busca_binaria_ativos(ativos_ordenados, alvo)
    print(f"\n--- BUSCA BINÁRIA ---")
    print(f"Ativo {alvo} encontrado na posição índice {idx}: {ativos_ordenados[idx]}")