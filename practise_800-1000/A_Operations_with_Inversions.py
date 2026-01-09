def solve(arr,n):
    count = 0
    largest_number = arr[0] # keep track of largest number
    # delete all numbers smaller than this
    for i in range(1,n):
        if arr[i] < largest_number:
            arr[i] = 'X'
            count += 1
        else:
            largest_number = arr[i]

    arr = [v for v in arr if v != 'X']
    print(count)

# number of test cases
t = int(input())
for _ in range(t):
    # size of array
    n = int(input())
    # array
    arr = list(map(int, input().split()))
    solve(arr, n)
