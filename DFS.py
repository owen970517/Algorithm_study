def dfs(graph, start_node, visit=list()):
   visit.append(start_node)
   print(start_node, end=' ')

   for node in graph[start_node]:
       if node not in visit:
           dfs(graph, node, visit)

graph = {
    '1' : ['2','5'],
    '2' : ['1','3','5'],
    '3' : ['2'],
    '4' :['7'],
    '5':    ['1','2','6'],
    '6' : ['5'],
    '7' :['4']
}
  
dfs(graph, '1')