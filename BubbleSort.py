def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t
nums=[2,5,4,6,7,1]
sort(nums)
print(nums)
