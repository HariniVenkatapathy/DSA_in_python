def maxsubarr(arr):
    neg = 0
    a1 = []
    for i in range(len(arr)-1):
        if arr[i]<0:
            neg = i
            arr.remove(arr[i])
        if neg<i and neg!=0:
            a1.append(arr[i])
            arr.remove(arr[i])
    print(arr)
    print(a1)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    maxsubarr(arr)
            
        
