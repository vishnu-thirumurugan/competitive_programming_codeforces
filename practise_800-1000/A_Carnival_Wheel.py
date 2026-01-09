def solve(arr):
    res = arr[a]
    for i in range(l):
        new_index = (a+i*b)%l
        res = max(res, arr[new_index])

    print(res)

t = int(input())
for _ in range(t):
    l,a,b = map(int, input().split())
    arr = [i for i in range(l)]
    solve(arr)