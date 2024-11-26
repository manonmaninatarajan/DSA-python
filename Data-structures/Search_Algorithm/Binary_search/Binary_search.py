def binary_search(arr,search):
    left=0
    right=len(arr)-1

    while left <=right:
        m = (left + right) // 2
        mid=arr[m]
        if(mid==search):
            print("the index of the number is:",m)
            return
        elif(mid<search):
            left=m+1
        else:
            right=m-1
    print("The number you entered is not in the list")
            
            
            
search=int(input("Enter the number want to search:"))        
arr=[11,12,13,14,15,16,17,18,19]
binary_search(arr,search)
