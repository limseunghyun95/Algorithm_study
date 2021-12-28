import sys

def dfs(graph, v, visited): # dfs 

    visited[v] = True
    dfs_result.append(v)
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v):
    
    from collections import deque
    
    need_visited = deque()
    visited = []
    
    need_visited.append(v)
    
    while need_visited:
        data = need_visited.popleft()
        if data not in visited:
            need_visited.extend(sorted(graph[data]))
            visited.append(data)
            
    return visited

n, m, v = map(int, sys.stdin.readline().split(" "))

graph = [[] for i in range(n+1)] # 그래프 초기화

for _ in range(m): # 그래프 데이터 입력
    
    n1, n2 = map(int, sys.stdin.readline().split(" "))
    
    graph[n1].append(n2)
    graph[n2].append(n1)
    
visited = [False] * (n+1) # 방문한 노드 기록을 위한 리스트

dfs_result = [] # dfs 실행 결과 담을 리스트

dfs(graph, v, visited) # dfs 실행

print(" ".join(map(str, dfs_result))) # dfs 결과 출력

bfs_result = bfs(graph, v)
print(" ".join(map(str, bfs_result))) # bfs 결과 출력