def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, num in enumerate(arr):
        for j in permutations(arr[:i] + arr[i+1:], n-1):
            result.append([num] + j)
    return result

permutation = permutations([1,2,3,4], 3)
print(permutation)