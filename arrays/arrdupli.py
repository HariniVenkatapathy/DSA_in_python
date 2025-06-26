def arrdupli(arr):
    res = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and arr[i]==arr[j]:
                res.add(arr[i])
    print(list(res))

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    arrdupli(arr)
