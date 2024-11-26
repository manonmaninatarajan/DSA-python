def bubblesort(arr):
  for j in range(0,len(arr)):
          for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
              temp=arr[i]
              arr[i]=arr[i+1]
              arr[i+1]=temp
            else:
               continue  
  print(arr)

arr=[1,2,5,3,8,3,4,6,4]
bubblesort(arr)
  
