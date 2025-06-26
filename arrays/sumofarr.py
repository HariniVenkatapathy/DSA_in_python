def sumofarr(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    sumofarr(arr)
