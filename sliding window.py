#sliding window is a technique used to solve problems that involve finding a contiguous subarray or substring that satisfies certain conditions. It involves maintaining a window of a certain size and sliding it across the input data to find the desired result.
arr = [2, 1, 5, 1, 3]
k = 3
n=len(arr)
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,n):
    window_sum+=arr[i]-arr[i-k]
    max_sum=max(max_sum,window_sum)
print(max_sum)