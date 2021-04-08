nums = [2,3,4,1,5]
l, r = 0, len(nums) - 1
while l < r:
    mid = (l + r) // 2
    print(l, r, mid)
    print(nums[l], nums[r], nums[mid])
    if nums[mid] < nums[r]:
        r = mid
    else:
        l = mid + 1
    print(l, r, mid)
    print(nums[l], nums[r], nums[mid])
    input()