def dfs(graph, start_node, visit=list()):
   visit.append(start_node)
   print(start_node, end=' ')
   
   for node in graph[start_node]:
       if node not in visit:
           dfs(graph, node, visit)
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
dfs(graph, 'A')