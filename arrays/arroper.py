def search(arr,x):
    return x in arr
def insert(arr,yi,y):
    if 0<=yi<=len(arr): #checking range of yi
        arr.insert(yi,y) #inserting the element
        return True
    return False
def remove(arr,z):
    if z in arr:
        arr.remove(z)
        return True
    return False

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    x = int(input())
    y = int(input())
    yi = int(input())
    z = int(input())
    print(search(arr, x), insert(arr, yi, y), remove(arr, z))
