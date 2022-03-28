def dfs(graph, start_node, visit=list()):
   visit.append(start_node)
   print(start_node, end=' ')
   
   for node in graph[start_node]:
       if node not in visit:
           dfs(graph, node, visit)
graph = {
    '1' : ['2','4'],
    '2' : ['3','4'],
    '3' : ['4']
}
  
dfs(graph, '1')