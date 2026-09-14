import random
import time
import sys
import csv
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "algoritmos"))

from quicksort import quicksort
from algoritmo02 import selection_sort
from algoritmo03 import merge_sort

sys.setrecursionlimit(200000)


def gerar_entradas(n, seed=42):
    random.seed(seed)
    aleatoria = [random.randint(0, 10**9) for _ in range(n)]
    ordenada = sorted(aleatoria)
    inversa = ordenada[::-1]
    return {"aleatoria": aleatoria, "ordenada": ordenada, "inversa": inversa}


def medir(func, arr):
    inicio = time.perf_counter()
    func(arr)
    fim = time.perf_counter()
    return round(fim - inicio, 4)


def main():
    tamanhos = [100, 1000, 10000, 100000]
    algoritmos = {
        "Quicksort": quicksort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
    }

    caminho_csv = os.path.join(os.path.dirname(__file__), "resultados.csv")
    with open(caminho_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "tipo", "algoritmo", "tempo_segundos"])

        for n in tamanhos:
            entradas = gerar_entradas(n)
            for tipo, arr in entradas.items():
                for nome, func in algoritmos.items():
                    # Selection Sort em n=100000 é Θ(n²) e fica excessivamente
                    # lento (dezenas de segundos). Pule se quiser evitar a espera.
                    if nome == "Selection Sort" and n == 100000:
                        writer.writerow([n, tipo, nome, "interrompido"])
                        print(f"n={n} tipo={tipo} {nome}: pulado (Θ(n²) muito lento)")
                        continue
                    t = medir(func, arr)
                    writer.writerow([n, tipo, nome, t])
                    print(f"n={n} tipo={tipo} {nome}: {t}s")

    print(f"\nResultados salvos em {caminho_csv}")


if __name__ == "__main__":
    main()
