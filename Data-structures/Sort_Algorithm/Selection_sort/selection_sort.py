def selection_sort(arr):
    for i in range(0,len(arr)):        
        min_index=i        
        for j in range((i+1),len(arr)):            
            if(arr[j]<arr[min_index]):
                min_index=j               
            else:
                continue
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
    print(arr)
        
   
  
arr=[19,3,2,5,56,28,49,12,23,34,43,65,10]

selection_sort(arr)
