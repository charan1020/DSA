#linear search is a simple searching algorithm that checks each element in the list one by one until it finds the target element or reaches the end of the list.
arr=[2,5,4,8,7]
key=2
n=len(arr)
for i in range(n):
    if arr[i]==key:
        print("Element found at index",i)
        break
    else:
        print("Error Element not found ")
        break
    
    
