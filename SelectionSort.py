def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        t = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = t

nums=[2,5,4,6,7,1]
sort(nums)
print(nums)
