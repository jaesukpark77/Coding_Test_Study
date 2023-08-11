n, b = map(int, input().split())
p = [int(input()) for _ in range(n)]

ans = 0

for i in range(n):
    tmp = [p[j] for j in range(n)]
    tmp[i] /= 2

    tmp.sort()

    student = 0
    cnt = 0

    for j in range(n):
        if cnt + tmp[j] > b:
            break
        cnt += tmp[j]
        student += 1
    
    ans = max(ans, student)

print(ans)