"""
Visualização de grafos e Caminho Hamiltoniano com NetworkX e Matplotlib.
Autora: Bruna Barbosa Portilho Bernardes
Data: 2025-10-26
"""

import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List, Optional
from main import encontrar_caminho_hamiltoniano

def desenhar_grafo_com_caminho(
    grafo: Dict[int, List[int]],
    caminho: Optional[List[int]],
    orientado: bool = False,
    titulo: str = "Visualização de Grafo"
):
    """
    Desenha o grafo e destaca o Caminho Hamiltoniano, se encontrado.
    """
    G = nx.DiGraph() if orientado else nx.Graph()

    for v, vizinhos in grafo.items():
        for u in vizinhos:
            G.add_edge(v, u)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(7, 5))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=700,
        font_weight="bold"
    )

    if caminho and len(caminho) > 1:
        arestas_caminho = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, edge_color="red", width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color="orange")
        plt.title(f"{titulo}\nCaminho Hamiltoniano: {caminho}\n(Feche para continuar)")
    else:
        plt.title(f"{titulo}\nNenhum Caminho Hamiltoniano encontrado.\n(Feche para continuar)")

    print(f"[VISUALIZAÇÃO] {titulo} - Feche o gráfico para ir para o próximo.")
    plt.show()


if __name__ == "__main__":
    exemplos = [
        {
            "nome": "Grafo Não Orientado 1",
            "grafo": {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2]},
            "orientado": False,
        },
        {
            "nome": "Digrafo 2",
            "grafo": {0: [1], 1: [2], 2: [3], 3: []},
            "orientado": True,
        },
        {
            "nome": "Grafo Não Orientado 3",
            "grafo": {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]},
            "orientado": False,
        },
        {
            "nome": "Digrafo 4",
            "grafo": {0: [1, 2], 1: [3], 2: [3], 3: []},
            "orientado": True,
        },
        {
            "nome": "Grafo Não Orientado 5",
            "grafo": {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]},
            "orientado": False,
        },
    ]

    for i, exemplo in enumerate(exemplos, 1):
        grafo = exemplo["grafo"]
        caminho = encontrar_caminho_hamiltoniano(grafo, len(grafo))
        print(f"\n[VISUALIZAÇÃO] Exemplo {i}: {exemplo['nome']}")
        desenhar_grafo_com_caminho(
            grafo,
            caminho,
            orientado=exemplo["orientado"],
            titulo=f"Exemplo {i}: {exemplo['nome']}"
        )
