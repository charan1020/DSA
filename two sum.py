arr=[2,5,4,8,7]
target=10
n=len(arr)
d=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            d.append((arr[i],arr[j]))
print(d)