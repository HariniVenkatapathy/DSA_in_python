def secondlarg(arr):
    lar = 0
    second = 0
    for i in range(len(arr)):
        if arr[i]>lar:
            lar = arr[i]
    for j in range(len(arr)):
        if arr[j]<lar and arr[j]>second:
            second = arr[j]
    print(second)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    secondlarg(arr)
