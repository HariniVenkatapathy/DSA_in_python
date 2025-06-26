def alternate(arr):
    for i in range(len(arr)):
        if i == 0 or i%2 == 0:
            print(arr[i],end = " ")

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    alternate(arr)
