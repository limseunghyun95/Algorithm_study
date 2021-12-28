# source : https://www.acmicpc.net/problem/2606

import sys
from collections import deque

def bfs(graph):
    
    visited = []    
    need_visited = deque()
    
    need_visited.append(1)
    
    while need_visited:
        data = need_visited.popleft()
        if data not in visited:
            visited.append(data)
            need_visited.extend(sorted(graph[data]))

    return visited

node_num = int(sys.stdin.readline())
edge_num = int(sys.stdin.readline())

graph = [[] for i in range(node_num+1)]

for _ in range(edge_num):
    
    node1, node2 = map(int, sys.stdin.readline().split(" "))

    graph[node1].append(node2)
    graph[node2].append(node1)
    

bfs_result = bfs(graph)

print(len(bfs_result) - 1) # 1번 컴퓨터를 통해 감연되는 컴퓨터 수를 출력하므로 1번 컴퓨터는 계산에서 제외