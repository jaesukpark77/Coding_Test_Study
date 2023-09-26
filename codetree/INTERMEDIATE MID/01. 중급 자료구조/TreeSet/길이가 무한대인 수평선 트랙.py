# problem link : https://www.codetree.ai/missions/8/problems/horizontal-track-with-infinite-length?&utm_source=clipboard&utm_medium=text

from sortedcontainers import SortedSet

n, t = map(int, input().split())
x, v = [], []

for _ in range(n):
    input_x, input_v = tuple(map(int, input().split()))
    x.append(input_x)
    v.append(input_v)

people_x = SortedSet()
event_t = SortedSet()

def add_event(x1, v1, x2, v2):
    if v1 <= v2:
        return
    
    event_t.add((1.0 * (x2 - x1) / (v1 - v2), x1, v1))

def remove_event(x1, v1, x2, v2):
    if v1 <= v2:
        return
    
    event_t.remove((1.0 * (x2 - x1) / (v1 - v2), x1, v1))

for i in range(n):
    people_x.add((x[i], v[i]))

for i in range(n - 1):
    add_event(x[i], v[i], x[i + 1], v[i + 1])

while event_t:
    curr_t, x, v = event_t[0]

    if curr_t > t:
        break

    people_x.remove((x, v))
    event_t.remove((curr_t, x, v))

    index = people_x.bisect_right((x, v))
    nx, nv = people_x[index]

    if index != 0:
        index -= 1
        px, pv = people_x[index]
        remove_event(px, pv, x, v)
        add_event(px, pv, nx, nv)

print(len(people_x))