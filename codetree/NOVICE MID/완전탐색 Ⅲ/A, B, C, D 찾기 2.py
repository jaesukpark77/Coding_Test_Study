# problem link : https://www.codetree.ai/missions/5/problems/find-a-b-c-d-2?&utm_source=clipboard&utm_medium=text

MAX_A = 40
MAX_N = 15

arr = list(map(int, input().split()))

for a in range(1, MAX_A + 1):
    for b in range(a, MAX_A + 1):
        for c in range(b, MAX_A + 1):
            for d in range(c, MAX_A + 1):
                arr2 = [a, b, c, d, a + b, b + c, c + d, d + a,
                    a + c, b + d, a + b + c, a + b + d, a + c + d, b + c + d,
                    a + b + c + d]

                
                if sorted(arr) == sorted(arr2):
                    print(a, b, c, d)