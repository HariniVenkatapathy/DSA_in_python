def max_value(arr,n):
    x=arr[0]
    for i in range(1,n):
        if arr[i]>x:
            x=arr[i]
        else:
            return x
if __name__ == '__main__':
    lst = []
 
# number of elements as input
    n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
    arr = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n] 
    result=max_value(arr,n)
    print("maximum value in array:",result)
