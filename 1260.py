from collections import deque

def dfs(graph, start_node, visit=list()):
   visit.append(start_node)
   print(start_node, end=' ')
   
   for node in graph[start_node]:
       if node not in visit:
           dfs(graph, node, visit)


def bfs (graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()


dfs(graph,V )
visited = [False] * (N+1)
print()
bfs(graph,V ,visited)

