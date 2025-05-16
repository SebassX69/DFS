from dfs import Graph

def main():
    # Crear el grafo
    g = Graph()
    
    # Agregar las aristas del grafo de ejemplo
    g.add_edge('A', 'B', weight=1)
    g.add_edge('A', 'C', weight=1)
    g.add_edge('B', 'D', weight=1)
    g.add_edge('B', 'E', weight=1)
    g.add_edge('C', 'F', weight=1)
    g.add_edge('E', 'G', weight=1)
    g.add_edge('F', 'H', weight=1)

    # Mostrar la estructura del grafo
    print("\nEstructura del grafo:")
    g.display()

    # Realizar y mostrar el recorrido DFS
    print("\nRecorrido DFS:")
    g.dfs_traversal('A')
    
    # Mostrar la visualización
    print("\n\nVisualización del recorrido DFS:")
    g.visualize_dfs()

if __name__ == "__main__":
    main() 