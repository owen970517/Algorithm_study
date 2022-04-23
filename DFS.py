def dfs(graph, start_node, visit=list()):
   visit.append(start_node)
   global count
   #print(start_node, end=' ')
   #print(visit)
   for node in graph[start_node]:
       if node not in visit:
           dfs(graph, node, visit)
           count+=1

graph = {
    '1' : ['2','5'],
    '2' : ['1','3','5'],
    '3' : ['2'],
    '4' :['7'],
    '5':  ['1','2','6'],
    '6' : ['5'],
    '7' :['4']
}
count=0
dfs(graph, '1')
print(count)