def sel_sor(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]< arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    for k in range(n):
        print(arr[k],end=" ")

if __name__=="__main__":
    user_input = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list and convert to integers
    arr = list(map(int, user_input.split()))
    
    sel_sor(arr)
