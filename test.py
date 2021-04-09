nums = [1,3,3]
nums = [2,2,2,0,2,2]
l, r = 0, len(nums) - 1
while l < r:
    mid = (l + r) // 2
    print(l, mid, r)
    print(nums[l], nums[mid], nums[r])
    if nums[mid] == nums[r]:
        r -= 1
    elif nums[mid] < nums[r]:
        r = mid
    else:
        l = mid + 1
    print(l, mid, r)
    print(nums[l], nums[mid], nums[r])
    input()
