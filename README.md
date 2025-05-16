# Implementación del Algoritmo DFS (Depth-First Search)

Este proyecto implementa el algoritmo de búsqueda en profundidad (DFS) para grafos en Python.

## Descripción

El algoritmo DFS (Depth-First Search o Búsqueda en Profundidad) es un algoritmo para recorrer o buscar en un grafo. Comienza en un nodo raíz y explora tan lejos como sea posible a lo largo de cada rama antes de retroceder.

## Características

- Implementación de un grafo usando diccionarios
- Soporte para grafos dirigidos y no dirigidos
- Soporte para aristas con peso
- Recorrido DFS con ordenamiento de vecinos
- Visualización del grafo

## Uso

1. Ejecuta el archivo `dfs.py`:
```bash
python dfs.py
```

2. El programa mostrará el recorrido DFS del grafo de ejemplo:
```
Recorrido DFS:
A B D E G C F H
```

## Estructura del Grafo de Ejemplo

El grafo de ejemplo tiene la siguiente estructura:
```
    A
   / \
  B   C
 / \   \
D   E   F
     \   \
      G   H
```

## Personalización

Para crear tu propio grafo, puedes modificar el código de ejemplo en `dfs.py`:

```python
g = Graph()
g.add_edge('Vértice1', 'Vértice2', weight=1)
g.add_edge('Vértice2', 'Vértice3', weight=1)
# ... más aristas ...

print("Recorrido DFS:")
g.dfs_traversal('Vértice1')
``` 