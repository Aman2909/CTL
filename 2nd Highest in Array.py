print("2nd highest number in the array")
arr = [124,53,11,34,76,98,65,762,33]
b=list(map(int,input().split()))
print(b)
if arr[0] > arr[1]:
    max = arr[0]
    max2 = arr[1]
else:
    max = arr[1]
    max2 = arr[0]
for x in range (2,len(arr)):
    if arr[x]>max:
        max2=max
        max=arr[x]
print(max2)