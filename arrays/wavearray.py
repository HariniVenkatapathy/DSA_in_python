def wavearray(arr):
    for i in range(0,len(arr)-1,2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    print(arr)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    wavearray(arr)
