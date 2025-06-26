def maxmin(arr):
    maxi = arr[0]
    mini = arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi = arr[i]
        if arr[i]<mini:
            mini = arr[i]
    print(mini ,end = " ")
    print(maxi)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    maxmin(arr)
               
