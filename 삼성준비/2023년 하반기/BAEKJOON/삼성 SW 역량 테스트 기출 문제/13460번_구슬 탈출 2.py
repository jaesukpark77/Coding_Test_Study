# problem link : https://www.acmicpc.net/problem/13460

from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def pos_init():
  rx, ry, bx, by = 0, 0, 0, 0

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 'R':
        rx, ry = i, j
      elif graph[i][j] == 'B':
        bx, by = i, j

  return rx, ry, bx, by

def bfs(rx, ry, bx, by):
  q = deque()
  q. append((rx, ry, bx, by))
  visited = []
  visited.append((rx, ry, bx, by))
  count = 0

  while q:
    for _ in range(len(q)):
      rx, ry, bx, by = q.popleft()
      if count > 10:
        print(-1)
        return
      if graph[rx][ry] == 'O':
        print(count)
        return
      
      for i in range(4):
        nrx, nry = rx, ry
        while True:
          nrx += dxs[i]
          nry += dys[i]

          if graph[nrx][nry] == '#':
            nrx -= dxs[i]
            nry -= dys[i]
            break
          if graph[nrx][nry] == 'O':
            break
        
        nbx, nby = bx, by
        while True:
          nbx += dxs[i]
          nby += dys[i]

          if graph[nbx][nby] == '#':
            nbx -= dxs[i]
            nby -= dys[i]
            break
          if graph[nbx][nby] == 'O':
            break
        
        if graph[nbx][nby] == 'O':
          continue
        if nrx == nbx and nry == nby:
          if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
            nrx -= dxs[i]
            nry -= dys[i]
          else:
            nbx -= dxs[i]
            nby -= dys[i]
        if (nrx, nry, nbx, nby) not in visited:
          q.append((nrx, nry, nbx, nby))
          visited.append((nrx, nry, nbx, nby))
    count += 1
  print(-1)

rx, ry, bx, by = pos_init()

bfs(rx, ry, bx, by)