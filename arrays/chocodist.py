def chocolatdist(arr,m):
    arr.sort()
    mini = arr[len(arr)-1]
    for i in range(len(arr)):
        for j in range(i+m-1,len(arr),1):
            temp = abs(arr[j]-arr[i])
            if temp<mini:
                mini = temp

    print(mini)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    m = int(input())
    chocolatdist(arr,m)
