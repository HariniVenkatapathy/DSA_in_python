def search(arr,x,y):
    n = len(arr)
    count = 0
    posx = 0
    posy = 0
    for i in range(n):
        if arr[i] == x:
            posx = count
            count += 1
        elif arr[i] == y:
            posy = count
            count += 1
        else:
            count += 1
        if posx>0 and posy>0:
            break
    

    print(posy - posx)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    x = int(input())
    y = int(input())
    search(arr,x,y)
