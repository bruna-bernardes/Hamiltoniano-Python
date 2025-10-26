"""
Algoritmo para encontrar Caminho Hamiltoniano em grafos orientados e não orientados.
Autora: Bruna Barbosa Portilho Bernardes
Data: 2025-10-26
"""

from typing import Dict, List, Optional

def encontrar_caminho_hamiltoniano(grafo: Dict[int, List[int]], n: int) -> Optional[List[int]]:
    """
    Encontra um Caminho Hamiltoniano usando o método de backtracking.
    Parâmetros:
        grafo (dict): dicionário de adjacência representando o grafo
        n (int): número total de vértices
    Retorna:
        Uma lista com o caminho Hamiltoniano se existir, ou None caso contrário.
    """
    caminho = []
    visitados = set()

    def backtrack(v: int) -> bool:
        """Função recursiva que tenta construir o caminho."""
        caminho.append(v)
        visitados.add(v)

        # Caso base: se todos os vértices foram visitados
        if len(caminho) == n:
            return True

        # Tenta visitar vizinhos não visitados
        for vizinho in grafo.get(v, []):
            if vizinho not in visitados:
                if backtrack(vizinho):
                    return True

        # Se não há vizinho viável, retrocede
        caminho.pop()
        visitados.remove(v)
        return False

    # Testa todos os vértices como possíveis pontos de partida
    for inicio in grafo:
        caminho.clear()
        visitados.clear()
        if backtrack(inicio):
            return caminho.copy()

    return None


if __name__ == "__main__":
    exemplos = [
        {
            "nome": "Grafo Não Orientado 1",
            "grafo": {
                0: [1, 2],
                1: [0, 2, 3],
                2: [0, 1, 3],
                3: [1, 2]
            },
            "orientado": False
        },
        {
            "nome": "Digrafo 2",
            "grafo": {
                0: [1],
                1: [2],
                2: [3],
                3: []
            },
            "orientado": True
        },
        {
            "nome": "Grafo Não Orientado 3",
            "grafo": {
                0: [1, 2],
                1: [0, 2],
                2: [0, 1, 3],
                3: [2]
            },
            "orientado": False
        },
        {
            "nome": "Digrafo 4",
            "grafo": {
                0: [1, 2],
                1: [3],
                2: [3],
                3: []
            },
            "orientado": True
        },
        {
            "nome": "Grafo Não Orientado 5",
            "grafo": {
                0: [1],
                1: [0, 2, 3],
                2: [1, 3],
                3: [1, 2]
            },
            "orientado": False
        }
    ]

    for i, exemplo in enumerate(exemplos, 1):
        grafo = exemplo["grafo"]
        n = len(grafo)
        print(f"\n=== Exemplo {i}: {exemplo['nome']} ===")
        print(f"Vértices: {list(grafo.keys())}")
        arestas = []
        for v, vizinhos in grafo.items():
            for u in vizinhos:
                if exemplo["orientado"] or (u, v) not in arestas:
                    arestas.append((v, u))
        print(f"Arestas: {arestas}")
        caminho = encontrar_caminho_hamiltoniano(grafo, n)
        if caminho:
            print(f"Caminho Hamiltoniano encontrado: {caminho}")
        else:
            print("Não existe Caminho Hamiltoniano neste grafo.")
