def productarr(arr):
    res = []
    for i in range(len(arr)):
        temp = 1
        for j in range(len(arr)):
            if arr[i] != arr[j]:
                temp *= arr[j]
        res.append(temp)
    print(res)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    productarr(arr)
