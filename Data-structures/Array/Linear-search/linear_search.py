print("Linear search algorithm")
print()

def linear_search(arr,value,j):
    for i in range(j):
        if arr[i]==value:
            print(i)
        else:
            continue
            
ans=[1,2,23,4,5,6,7,8]
j=len(ans)
value=int(input("enter the value to search"))
linear_search(ans,value,j)
