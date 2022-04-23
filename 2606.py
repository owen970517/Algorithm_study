def dfs(graph, start_node, visit=list()):
   visit.append(start_node)
   global count
   for node in graph[start_node]:
       if node not in visit:
           dfs(graph, node, visit)
           count+=1

n=int(input())
s=int(input())
graph = [[] for _ in range(n+1)]
for _ in range(s):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
dfs(graph,1)
print(count)


