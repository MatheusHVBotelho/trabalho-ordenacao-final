# Exercícios resolvidos

## 1ª) Vetor-exemplo demonstrando instabilidade do Selection Sort

**Pergunta:** Invente um vetor-exemplo de entrada para demonstrar que a ordenação por seleção é um método instável. Mostre os passos da execução do algoritmo até que a instabilidade seja violada.

**Resposta:** Considere o vetor [5, 2, 8, 1, 4]. Na ordenação por seleção, primeiro encontramos o menor elemento (1) e colocamos na 1ª posição. Depois, procuramos o menor entre os elementos restantes e repetimos o processo até que o vetor esteja ordenado. Ao final obtemos [1, 2, 4, 5, 8].

## 2ª) Tornando o Quicksort estável

**Pergunta:** Quicksort não é um algoritmo estável (Guedes Neto, 2003). Que tipo de transformação você poderia fazer nas chaves para que ele se torne um algoritmo estável? Discuta se a transformação é independente da natureza da chave.

**Resposta:** Para tornar o Quicksort estável, anexa-se a cada chave a posição original do elemento no vetor, e passa-se a comparar o par (chave, posição) em vez de só a chave. Essa técnica é independente do tipo de chave, só custa um pouco mais de espaço (guardar os índices) e comparação (comparar os dois valores do par).

## 3ª) Quicksort — particionamento

**a)** Mostre como o vetor A B A B A B A é particionado quando se escolhe o elemento do meio, A[(esq + dir) / 2], como pivô.

A B A B A B A → troca posição 2 e posição 7 → fica A A A B A B B

**b)** Mostre as etapas de funcionamento do Quicksort para ordenar as chaves Q U I C K S O R T. Considere que o pivô escolhido é o elemento do meio A[(esq + dir) / 2].

```
Q U I C K S O R T
Pivô = K
Primeira troca: Q => K e U => C = K C I U Q S O R T
Pivô = C
Segunda troca: C => K = C K I U Q S O R T e K => I = C I K U Q S O R T
Pivô = S
Terceira troca: U => R e Q => O = R Q O S U T
Pivô = Q
Quarta troca: U => R e Q => O = R Q O S U T
Pivô = U
Quinta troca: U => T = S T U
Juntando tudo fica => C I K O Q R S T U
```

## 4ª) Operadores de fila de prioridade (Heap)

**Pergunta:** Implemente os operadores HeapConstrói, RetiraMin, DiminuiChave e Insere para realizar as seguintes operações. Considere o conjunto inicial [20, 15, 8, 10, 5, 12, 3].

**A) Construir uma fila de prioridade a partir de um conjunto com n itens**
Usamos HeapConstroi para transformar o conjunto em um Min-Heap. Após a construção: [3, 5, 8, 10, 15, 12, 20]. A propriedade do Min-Heap é respeitada porque cada pai possui uma chave menor ou igual às de seus filhos.

**B) Informar qual o menor item do conjunto**
Como estamos usando Min-Heap, o menor elemento está sempre na raiz: Menor = H[0]. Para o nosso exemplo: Menor item = 3. Complexidade: O(1).

**C) Retirar o item com menor chave**
Usamos RetiraMin: retiramos o elemento da raiz (3), colocamos o último elemento (20) na raiz e reorganizamos o Heap.
Antes: [3, 5, 8, 10, 15, 12, 20] → Depois de retirar 3: [20, 5, 8, 10, 15, 12] → Reorganizado: [5, 10, 8, 20, 15, 12]
RetiraMin() -> 3. Complexidade: O(log n).

**D) Inserir um novo item**
Suponha que queremos inserir 2. Colocamos o elemento no final: [5, 10, 8, 20, 15, 12, 2]. Comparamos com o pai e trocamos enquanto necessário: [5, 10, 2, 20, 15, 12, 8] → [2, 10, 5, 20, 15, 12, 8]. Complexidade: O(log n).

**E) Diminuir o valor da chave do item i para um novo valor menor que o atual**
Suponha que o elemento 20 tenha sua chave diminuída para 1.
Antes: [2, 10, 5, 20, 15, 12, 8] → Alteramos 20 -> 1: [2, 10, 5, 1, 15, 12, 8] → Como 1 ficou menor que seu pai (10), subimos o elemento: [2, 1, 5, 10, 15, 12, 8] → [1, 2, 5, 10, 15, 12, 8]. Complexidade: O(log n).

---

## Questões pendentes (a preencher)

Espaço reservado para as 2 questões ainda não fornecidas pelo enunciado.
