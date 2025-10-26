
# Projeto Caminho Hamiltoniano (FPAA)

📖 **O que é este projeto?**  
Este projeto implementa, em Python, um algoritmo para **encontrar um Caminho Hamiltoniano** em um grafo (orientado ou não). O trabalho atende ao enunciado da disciplina *Fundamentos de Projeto e Análise de Algoritmos (FPAA)* e contém código (`main.py`), documentação (este README) e uma ferramenta opcional de visualização (`view.py`) que salva a imagem do grafo com o caminho destacado.

---

## 🧭 O que é um Caminho Hamiltoniano?
Um **Caminho Hamiltoniano** é uma sequência de vértices que visita cada vértice do grafo exatamente uma vez. Decidir se existe tal caminho é um problema clássico em teoria dos grafos e está associado a dificuldades computacionais (NP-Completo).

---

## 🔑 Principais pontos
- Implementação baseada em **backtracking** (busca com retorno).
- Funciona para **grafos direcionados** e **não-direcionados**.
- Inclui um módulo opcional de **visualização** utilizando `networkx` e `matplotlib`.

---

## ▶️ Como executar o projeto

### Pré-requisitos
- Python 3.9+ (recomendado 3.11)
- (Opcional para visualizar) `networkx` e `matplotlib`:
- bash
- pip install networkx matplotlib

### Clonar
- git clone https://github.com/bruna-bernardes/Hamiltoniano-Python.git
cd Hamiltoniano-Python

---

## Exemplo de saída

=== Exemplo 1: Grafo Não Orientado 1 ===
Vértices: [0, 1, 2, 3]
Arestas: [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
Caminho Hamiltoniano encontrado: [0, 1, 2, 3]

---

## 📊 Análise de complexidade
Classes de complexidade

P: problemas resolvidos em tempo polinomial.
→ O Caminho Hamiltoniano não pertence a P.

NP: soluções verificáveis em tempo polinomial.

NP-Completo: classe onde o problema se enquadra.

NP-Difícil: engloba problemas tão ou mais complexos que os NP-Completo.

O Caminho Hamiltoniano é NP-Completo, pois o TSP pode ser reduzido a ele em tempo polinomial.

---

## Complexidade temporal

Pior caso: 
𝑂(𝑛!)
O(n!), onde n é o número de vértices.
(Testa todas as possíveis permutações de vértices)

Melhor caso: 
𝑂(𝑛)
O(n) — quando o primeiro caminho testado é válido.

Espaço: 
𝑂(𝑛)
O(n), para armazenar o caminho e os vértices visitados.

## Teorema Mestre

O Teorema Mestre não se aplica, pois o algoritmo não segue um padrão de divisão e conquista T(n)=aT(n/b)+f(n)).
Aqui, a recursão depende da estrutura do grafo e não do tamanho dividido do problema.

---

## ⚙️ Complexidade Ciclomática

A função recursiva backtrack possui:

Nós (N): 6

Arestas (E): 8

Componentes (P): 1

Aplicando a fórmula:

M=E−N+2P=8−6+2(1)=4

---

## ✅ Conclusão

O algoritmo implementado é uma solução exata e didática para o problema do Caminho Hamiltoniano.
Embora tenha complexidade exponencial, é eficaz para grafos pequenos e demonstra com clareza os conceitos de busca com retrocesso e complexidade NP.
