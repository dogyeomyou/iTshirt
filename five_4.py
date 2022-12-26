# -*- coding: utf-8 -*-
# five_3.py
# 반복적으로 구현한 n! 함수
def factorial_interative(n):
    result = 1
    #
    for i in range(1, n+1):
        result *= i
# -*- coding: utf-8 -*-
# five_5.py

#DFS 메소드 정의
def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적을 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph =[
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]
#각 노드가 방문된 정보를 표시
visited = [False]*9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)            

