# problem link : https://school.programmers.co.kr/learn/courses/30/lessons/72413

# Floyd Warshall Method
import sys            

def solution(n, s, a, b, fares):
    MAX_INT = sys.maxsize
    answer = MAX_INT
    cost = [[MAX_INT] * (n + 1) for _ in range(n+1)]
    
    def floyd_warshall():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
                    
    
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
        
    floyd_warshall()
    
    for i in range(1, n+1):
        answer = min(answer, cost[s][i] + cost[i][a] + cost[i][b])
    
    return answer

# Dijkstra Method

import heapq
import sys

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for f in fares:
        x, y, z = f[0], f[1], f[2]
        graph[x].append((y, z))
        graph[y].append((x, z))
    
    def dijkstra(n, start, end):
        MAX_INT = sys.maxsize
        dist = [MAX_INT] * (n+1)
        pq = []
        heapq.heappush(pq, (0, start))
        dist[start] = 0
        
        while pq:
            min_dist, min_index = heapq.heappop(pq)

            if min_dist != dist[min_index]:
                continue

            for target_index, target_dist in graph[min_index]:
                new_dist = dist[min_index] + target_dist
                if dist[target_index] > new_dist:
                    dist[target_index] = new_dist
                    heapq.heappush(pq, (new_dist, target_index))
                    
        return dist[end]

    result = []
    for p in range(1, n +1):
        if p != s:
            s_to_p = dijkstra(n,s,p)
            p_to_a = dijkstra(n,p,a)
            p_to_b = dijkstra(n,p,b)
            result.append(s_to_p+p_to_a+p_to_b)
        else:
            result.append(dijkstra(n,s,a)+dijkstra(n,s,b))
    
    return min(result)