import matplotlib.pyplot as plt

def insertion_sort(arr):
    i=1
    while i<len(arr):
        j=i
        while j>0 and arr[j-1] > arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j=j-1
        i=i+1 
    print(arr)

arr=[1,4,3,6,34,2,8,6,67,96,45,23,12]
insertion_sort(arr)
