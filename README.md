# Trabalho de Algoritmos de Ordenação

Implementação, análise e experimentos com três algoritmos de ordenação: **Quicksort**, **Selection Sort** e **Merge Sort**.

Disciplina: Algoritmo e complexidade
Alunos: Bárbara Marjorye, Giselane Maria, Matheus Henrique, Diego Assis

## Estrutura do repositório

```
trabalho-ordenacao/
├── README.md
├── exercicios/
│   └── exercicios.md          # Questões teóricas resolvidas (1 a 4)
├── algoritmos/
│   ├── quicksort.py            # Algoritmo Quicksort
│   ├── selectionsort.py          # Selection Sort
│   └── mergesort.py          # Merge Sort
├── experimentos/
│   ├── experimento.py          # Script que roda os testes de tempo
│   └── resultados.csv          # Resultados medidos (tempo em segundos)
└── graficos/
    ├── gerar_graficos.py       # Script que gera os gráficos a partir do CSV
    ├── comparativo_por_tipo.png
    └── quicksort_vs_mergesort.png
```

## Como executar

Requer Python 3.

Rodar um algoritmo isolado:

```bash
python3 algoritmos/quicksort.py
```

Rodar todos os experimentos de tempo (gera experimentos/resultados.csv):

```bash
python3 experimentos/experimento.py
```

Gerar os gráficos comparativos (requer `matplotlib`):

```bash
pip install matplotlib
python3 graficos/gerar_graficos.py
```

## Resumo dos resultados

| Algoritmo | Melhor caso | Médio | Pior caso | Espaço |
|---|---|---|---|---|
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

Os experimentos usaram vetores de 100, 1.000, 10.000 e 100.000 elementos, com entradas aleatória, ordenada e inversa. O Selection Sort em n = 100.000 foi interrompido após 90 segundos sem terminar, por causa do crescimento Θ(n²). Detalhes completos em `experimentos/resultados.csv` e nos gráficos em `graficos/`.
