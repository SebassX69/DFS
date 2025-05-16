import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Graph:
    def __init__(self):
        # Constructor de la clase Graph. Inicializa un diccionario para representar el grafo.
        self.graph = {}
        self.nx_graph = nx.Graph()  # Grafo de NetworkX para visualización
        self.visit_order = []  # Lista para almacenar el orden de visita

    def add_vertex(self, vertex):
        # Método para agregar un vértice al grafo.
        if vertex not in self.graph:
            # Si el vértice no está en el grafo, lo agrega con un diccionario vacío para representar sus conexiones.
            self.graph[vertex] = {}
            self.nx_graph.add_node(vertex)

    def add_edge(self, vertex1, vertex2, weight=None, directed=False):
        # Método para agregar una arista al grafo entre dos vértices dados.
        self.add_vertex(vertex1)  # Aseguramos que los vértices estén presentes en el grafo.
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight  # Añade una conexión desde vertex1 a vertex2 con el peso dado.
        self.nx_graph.add_edge(vertex1, vertex2, weight=weight)

        if not directed:
            # Si el grafo no es dirigido, añade también una conexión desde vertex2 a vertex1 con el mismo peso.
            self.graph[vertex2][vertex1] = weight

    def display(self):
        # Método para mostrar el grafo en forma legible.
        for vertex, edges in self.graph.items():
            print(f"Vértice {vertex} tiene como conexiones a:")
            for neighbor, weight in edges.items():
                if weight:
                    # Si hay peso en la conexión, imprime el vecino y su peso.
                    print(f"  - {neighbor} (peso: {weight})")
                else:
                    # Si no hay peso, imprime solo el vecino.
                    print(f"  - {neighbor}")

    def dfs_traversal(self, start_vertex, visited=None):
        # Método para realizar un recorrido en profundidad (Depth-First Search) desde un vértice dado.
        if visited is None:
            # Si no se proporciona un conjunto de vértices visitados, lo inicializamos como un conjunto vacío.
            visited = set()
            self.visit_order = []  # Reiniciamos el orden de visita

        visited.add(start_vertex)  # Agregamos el vértice actual a los visitados.
        self.visit_order.append(start_vertex)  # Guardamos el orden de visita
        print(start_vertex, end=" ")  # Imprimimos el vértice actual.
        
        neighbors = self.graph[start_vertex]  # Obtenemos los vecinos del vértice actual.
        sorted_neighbors = sorted(neighbors, key=lambda x: neighbors[x])
        # Ordenamos los vecinos por orden ascendente de acuerdo al peso de la arista que los conecta.

        for neighbor in sorted_neighbors:
            # Recorremos los vecinos ordenados.
            if neighbor not in visited:
                # Si el vecino no ha sido visitado aún, realizamos una llamada recursiva para visitarlo.
                self.dfs_traversal(neighbor, visited)

    def visualize_dfs(self):
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.nx_graph)
        
        def update(frame):
            plt.clf()
            # Dibujar el grafo base
            nx.draw(self.nx_graph, pos, with_labels=True, 
                   node_color='lightgray', node_size=1500, 
                   font_size=16, font_weight='bold')
            
            # Resaltar los nodos visitados hasta el momento
            if frame < len(self.visit_order):
                visited_nodes = self.visit_order[:frame+1]
                nx.draw_networkx_nodes(self.nx_graph, pos, 
                                     nodelist=visited_nodes,
                                     node_color='lightgreen',
                                     node_size=1500)
                
                # Dibujar las aristas del recorrido
                if frame > 0:
                    edges = [(self.visit_order[i], self.visit_order[i+1]) 
                            for i in range(frame)]
                    nx.draw_networkx_edges(self.nx_graph, pos, 
                                         edgelist=edges,
                                         edge_color=['green'] * len(edges),
                                         width=2)
            
            plt.title(f"Recorrido DFS - Paso {frame+1}/{len(self.visit_order)}")
            plt.axis('off')
        
        # Crear la animación
        anim = FuncAnimation(plt.gcf(), update, 
                           frames=len(self.visit_order),
                           interval=1000,  # 1 segundo entre frames
                           repeat=False)
        
        plt.show()

# Ejemplo de uso:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', weight=1)
    g.add_edge('A', 'C', weight=1)
    g.add_edge('B', 'D', weight=1)
    g.add_edge('B', 'E', weight=1)
    g.add_edge('C', 'F', weight=1)
    g.add_edge('E', 'G', weight=1)
    g.add_edge('F', 'H', weight=1)

    print("Recorrido DFS:")
    g.dfs_traversal('A')
    print("\n\nVisualización del recorrido DFS:")
    g.visualize_dfs() 