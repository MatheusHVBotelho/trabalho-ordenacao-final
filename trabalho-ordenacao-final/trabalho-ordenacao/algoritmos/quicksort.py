def quicksort(arr):
    """Ordena usando o método de particionamento (divisão e conquista)."""
    if len(arr) <= 1:
        return arr

    pivo = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]

    return quicksort(menores) + iguais + quicksort(maiores)


if __name__ == "__main__":
    dados = [64, 25, 12, 22, 11, 90, 5]
    print("Original: ", dados)
    print("Ordenado: ", quicksort(dados))
