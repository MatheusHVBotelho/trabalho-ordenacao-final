def merge_sort(arr):
    """Ordena dividindo o array recursivamente e depois mesclando as partes."""
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return _merge(esquerda, direita)


def _merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


if __name__ == "__main__":
    dados = [64, 25, 12, 22, 11, 90, 5]
    print("Original: ", dados)
    print("Ordenado: ", merge_sort(dados))
