def stockbuy(arr):
   stock  = 0
   for i in range(len(arr)-1):
       if arr[i]<arr[i+1]:
           stock += abs(arr[i+1]-arr[i])
   print(stock)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    stockbuy(arr)
            
