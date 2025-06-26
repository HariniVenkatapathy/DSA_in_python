def reversearr(arr):
    arr1 = []
    for i in range(len(arr)-1,-1,-1): #the range function needs a step value so -1
        arr1.append(arr[i])
    print(arr1)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    reversearr(arr)
