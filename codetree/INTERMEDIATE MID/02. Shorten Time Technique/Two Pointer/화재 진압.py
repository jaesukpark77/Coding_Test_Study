# problem link : https://www.codetree.ai/missions/8/problems/fire-suppression?&utm_source=clipboard&utm_medium=text

n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

def dist(i, j):
    return abs(fires[i] - stations[j])

def put_out_fire():
    max_dist = 0

    j = 1

    for i in range(1, n+1):
        while j + 1 <= m and dist(i, j) > dist(i, j + 1):
            j += 1
        
        max_dist = max(max_dist, dist(i, j))

    return max_dist

fires = [0] + sorted(fires)
stations = [0] + sorted(stations)

print(put_out_fire())