import networkx as nx
from collections import deque
import math

def bfs_with_networkx(graph, start):
    nx.set_node_attributes(graph, 'WHITE', 'color')
    nx.set_node_attributes(graph, float('inf'), 'distance')
    nx.set_node_attributes(graph, None, 'predecessor')

    graph.nodes[start]['color'] = 'GRAY'
    graph.nodes[start]['distance'] = 0
    graph.nodes[start]['predecessor'] = None

    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph.neighbors(current):
            if graph.nodes[neighbor]['color'] == 'WHITE':
                graph.nodes[neighbor]['color'] = 'GRAY'
                graph.nodes[neighbor]['distance'] = graph.nodes[current]['distance'] + 1
                graph.nodes[neighbor]['predecessor'] = current
                queue.append(neighbor)
        graph.nodes[current]['color'] = 'BLACK'

    distances = {node: graph.nodes[node]['distance'] for node in graph.nodes}
    return distances

def calculate_graph_metrics(graph):
    vertices = graph.number_of_nodes()
    edges = graph.number_of_edges()
    degrees = [degree for _, degree in graph.degree()]
    gmin = min(degrees)
    gmax = max(degrees)
    gmed = sum(degrees) / vertices

    connected_components = list(nx.connected_components(graph))
    diam = 0
    for component in connected_components:
        subgraph = graph.subgraph(component)
        for node in subgraph:
            distances = bfs_with_networkx(subgraph, node)
            max_distance = max(
                dist for dist in distances.values() if dist < float('inf')
            )
            diam = max(diam, max_distance)

    # 1 componente a mais = diametro infinito
    if len(connected_components) > 1:
        diam = float('inf')

    return vertices, edges, gmin, gmax, gmed, diam

def main():
    print("V   E   gmin gmax gmed diam")
    print("-----------------------------------------------")
    for v in range(10, 210, 10):
        graph = nx.gnm_random_graph(v, v * 2)  # grafo aleatório com v vértices e 2*v arestas. não mexa nisso!
        vertices, edges, gmin, gmax, gmed, diam = calculate_graph_metrics(graph)
        print(f"{vertices:<3} {edges:<3} {gmin:<4} {gmax:<4} {gmed:<4.1f} {diam:<4}")

if __name__ == "__main__":
    main()
