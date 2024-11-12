import random
import networkx as nx

def generate_graph(n, p):
    """Gera um grafo com n vértices e probabilidade p para criação das arestas."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                G.add_edge(u, v)
    
    return G

def graph_properties(G):
    """Calcula as propriedades do grafo: número de vértices, arestas, graus e diâmetro."""
    num_vertices = G.number_of_nodes()
    num_edges = G.number_of_edges()
    
    degrees = [degree for _, degree in G.degree()]
    min_degree = min(degrees) if degrees else 0
    max_degree = max(degrees) if degrees else 0
    avg_degree = sum(degrees) / num_vertices if num_vertices > 0 else 0
    
    try:
        diameter = nx.diameter(G) if nx.is_connected(G) else float('inf')
    except nx.NetworkXError:
        diameter = float('inf')
    
    return num_vertices, num_edges, min_degree, max_degree, avg_degree, diameter

def main():
    ini, fim, stp, p = 10, 200, 10, 0.1  # Exemplo de parâmetros de entrada
    results = []
    
    for n in range(ini, fim + 1, stp):
        G = generate_graph(n, p)
        V, E, gmin, gmax, gmed, diam = graph_properties(G)
        results.append((V, E, gmin, gmax, gmed, diam))
    
    # Exibir resultados
    print("V E gmin gmax gmed diam")
    print("-----------------------------------------------")
    for result in results:
        print(f"{result[0]} {result[1]} {result[2]} {result[3]} {result[4]:.1f} {result[5]}")
    
if __name__ == "__main__":
    main()
