nums = [1,2,3,4,5,6]
target=9
nums1 = nums.copy()
nums1.sort()
start = 0
end = len(nums1)-1
arr = []
while start < end:
    if nums1[start] + nums1[end] == target:
        n1 = nums1[start]
        n2 = nums1[end]
        break
    elif nums1[start] + nums1[end] > target: 
        end-=1
    else:
        start+=1
for i in range(len(nums)):
    if nums[i] == n1:
        arr.append(i)
    elif nums[i] == n2:
        arr.append(i)
print(arr)
