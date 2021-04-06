nums = [1,2]
i = 2
for j in range(2, len(nums)):
    if nums[j] != nums[i-2]:
        nums[i] = nums[j]
        i += 1
print(nums,i)