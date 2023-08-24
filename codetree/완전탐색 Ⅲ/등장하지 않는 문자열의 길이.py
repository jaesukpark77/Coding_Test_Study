# problem link : https://www.codetree.ai/missions/5/problems/length-of-string-that-does-not-appear?&utm_source=clipboard&utm_medium=text

n = int(input())
string = input()

ans = 1

for i in range(1, n):
    twice = False

    for j in range(n - i + 1):
        for k in range(j + 1, n - i + 1):
            issame = True

            for l in range(i):
                if string[j + l] != string[k + l]:
                    issame = False
            
            if issame:
                twice = True

    if twice:
        ans = i + 1
    else:
        break

print(ans)