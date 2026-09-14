import csv
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CAMINHO_CSV = os.path.join(os.path.dirname(__file__), "..", "experimentos", "resultados.csv")

tamanhos = [100, 1000, 10000, 100000]
tipos = ["aleatoria", "ordenada", "inversa"]
titulos = {"aleatoria": "Entrada Aleatória", "ordenada": "Entrada Ordenada (crescente)", "inversa": "Entrada Inversa (decrescente)"}
algoritmos = ["Quicksort", "Selection Sort", "Merge Sort"]
cores = {"Quicksort": "#2563eb", "Selection Sort": "#dc2626", "Merge Sort": "#16a34a"}

# Valor estimado (extrapolado) para Selection Sort em n=100000, ja que a execucao foi interrompida
ESTIMATIVA_SELECTION_100K = 130.0


def carregar_resultados():
    resultados = {n: {t: {} for t in tipos} for n in tamanhos}
    with open(CAMINHO_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n = int(row["n"])
            tipo = row["tipo"]
            alg = row["algoritmo"]
            valor = row["tempo_segundos"]
            resultados[n][tipo][alg] = ESTIMATIVA_SELECTION_100K if valor == "interrompido" else float(valor)
    return resultados


def main():
    resultados = carregar_resultados()
    pasta_saida = os.path.dirname(__file__)

    # Grafico 1: um painel por tipo de entrada
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    for ax, tipo in zip(axes, tipos):
        for alg in algoritmos:
            valores = [resultados[n][tipo][alg] for n in tamanhos]
            estilo = "--" if alg == "Selection Sort" else "-"
            ax.plot([str(n) for n in tamanhos], valores, marker="o", label=alg, color=cores[alg], linestyle=estilo)
        ax.set_yscale("log")
        ax.set_title(titulos[tipo], fontsize=11)
        ax.set_xlabel("Tamanho do vetor (n)")
        ax.set_ylabel("Tempo (s) - escala log")
        ax.grid(True, which="both", alpha=0.3)
        ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, "comparativo_por_tipo.png"), dpi=150)
    plt.close()

    # Grafico 2: apenas Quicksort x Merge Sort
    fig, ax = plt.subplots(figsize=(8, 5))
    for alg in ["Quicksort", "Merge Sort"]:
        for tipo, estilo, marcador in zip(tipos, ["-", "--", ":"], ["o", "s", "^"]):
            valores = [resultados[n][tipo][alg] for n in tamanhos]
            ax.plot([str(n) for n in tamanhos], valores, marker=marcador, linestyle=estilo,
                    label=f"{alg} - {titulos[tipo]}", color=cores[alg], alpha=0.85)
    ax.set_xlabel("Tamanho do vetor (n)")
    ax.set_ylabel("Tempo (s)")
    ax.set_title("Quicksort x Merge Sort - detalhe (Θ(n log n) em todos os casos)")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta_saida, "quicksort_vs_mergesort.png"), dpi=150)
    plt.close()

    print("Graficos gerados com sucesso em", pasta_saida)


if __name__ == "__main__":
    main()
