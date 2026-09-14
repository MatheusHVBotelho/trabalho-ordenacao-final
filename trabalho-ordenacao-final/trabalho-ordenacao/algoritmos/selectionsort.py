def selection_sort(arr):
    """Ordena selecionando repetidamente o menor elemento restante."""
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        indice_menor = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        arr[i], arr[indice_menor] = arr[indice_menor], arr[i]

    return arr


if __name__ == "__main__":
    dados = [64, 25, 12, 22, 11, 90, 5]
    print("Original: ", dados)
    print("Ordenado: ", selection_sort(dados))
