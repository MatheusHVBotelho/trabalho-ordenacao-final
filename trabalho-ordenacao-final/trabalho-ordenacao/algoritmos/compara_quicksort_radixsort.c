/*
 * Compara o tempo de execucao de Quicksort (baseado em comparacoes) e
 * Radix Sort (LSD, byte a byte) para ordenar N cadeias de caracteres de
 * tamanho fixo L, em ordem aleatoria.
 *
 * Uso: ./compara N L SEED
 *   N    = quantidade de registros
 *   L    = tamanho da chave (numero de caracteres)
 *   SEED = semente do gerador aleatorio (mesma semente = mesmos dados)
 *
 * Imprime uma linha CSV: L,tempo_quicksort_segundos,tempo_radix_segundos
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

static uint64_t rng_state;

static uint64_t xorshift64(void) {
    uint64_t x = rng_state;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    rng_state = x;
    return x;
}

static double agora_segundos(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

/* ---------- Quicksort (pivo = elemento do meio, opera em ponteiros) ---------- */

static int L_global;

static void trocar(unsigned char **a, unsigned char **b) {
    unsigned char *tmp = *a;
    *a = *b;
    *b = tmp;
}

static void quicksort_rec(unsigned char **v, long esq, long dir) {
    while (esq < dir) {
        long meio = esq + (dir - esq) / 2;
        unsigned char *pivo = v[meio];
        long i = esq, j = dir;
        while (i <= j) {
            while (memcmp(v[i], pivo, L_global) < 0) i++;
            while (memcmp(v[j], pivo, L_global) > 0) j--;
            if (i <= j) {
                trocar(&v[i], &v[j]);
                i++;
                j--;
            }
        }
        /* recursao na particao menor, loop na maior (evita estouro de pilha) */
        if (j - esq < dir - i) {
            quicksort_rec(v, esq, j);
            esq = i;
        } else {
            quicksort_rec(v, i, dir);
            dir = j;
        }
    }
}

/* ---------- Radix Sort LSD (byte a byte, contagem estavel) ---------- */

static void radix_sort(unsigned char **v, long n, int L) {
    unsigned char **buf = malloc(n * sizeof(unsigned char *));
    long count[257];
    for (int pos = L - 1; pos >= 0; pos--) {
        memset(count, 0, sizeof(count));
        for (long i = 0; i < n; i++) count[(unsigned char)v[i][pos] + 1]++;
        for (int k = 0; k < 256; k++) count[k + 1] += count[k];
        for (long i = 0; i < n; i++) buf[count[(unsigned char)v[i][pos]]++] = v[i];
        memcpy(v, buf, n * sizeof(unsigned char *));
    }
    free(buf);
}

static int esta_ordenado(unsigned char **v, long n, int L) {
    for (long i = 1; i < n; i++)
        if (memcmp(v[i - 1], v[i], L) > 0) return 0;
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "Uso: %s N L SEED\n", argv[0]);
        return 1;
    }
    long n = atol(argv[1]);
    int L = atoi(argv[2]);
    rng_state = (uint64_t)atol(argv[3]) | 1;
    L_global = L;

    /* gera o bloco de dados: n strings de L caracteres minusculos aleatorios */
    unsigned char *dados = malloc((size_t)n * L);
    for (long i = 0; i < n * (long)L; i++) {
        dados[i] = 'a' + (xorshift64() % 26);
    }

    /* array de ponteiros na ordem original (mesma para os dois algoritmos) */
    unsigned char **original = malloc(n * sizeof(unsigned char *));
    for (long i = 0; i < n; i++) original[i] = dados + (size_t)i * L;
    /* embaralha a ordem dos ponteiros (posicoes), mantendo os dados fixos */
    for (long i = n - 1; i > 0; i--) {
        long j = xorshift64() % (i + 1);
        trocar(&original[i], &original[j]);
    }

    unsigned char **copiaA = malloc(n * sizeof(unsigned char *));
    unsigned char **copiaB = malloc(n * sizeof(unsigned char *));
    memcpy(copiaA, original, n * sizeof(unsigned char *));
    memcpy(copiaB, original, n * sizeof(unsigned char *));

    double t0 = agora_segundos();
    quicksort_rec(copiaA, 0, n - 1);
    double t1 = agora_segundos();
    double tempo_quicksort = t1 - t0;
    if (!esta_ordenado(copiaA, n, L)) {
        fprintf(stderr, "ERRO: quicksort nao ordenou corretamente\n");
        return 1;
    }

    double t2 = agora_segundos();
    radix_sort(copiaB, n, L);
    double t3 = agora_segundos();
    double tempo_radix = t3 - t2;
    if (!esta_ordenado(copiaB, n, L)) {
        fprintf(stderr, "ERRO: radix sort nao ordenou corretamente\n");
        return 1;
    }

    printf("%d,%.4f,%.4f\n", L, tempo_quicksort, tempo_radix);

    free(dados);
    free(original);
    free(copiaA);
    free(copiaB);
    return 0;
}
