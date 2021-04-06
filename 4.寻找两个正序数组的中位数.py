#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1   # 始终保证nums1较小
            # return self.findMedianSortedArrays(nums2, nums1)
        infinity = 2**30
        m, n = len(nums1),len(nums2)
        l, r = 0, m
        while l <= r:
            i = (l + r)//2
            j = (m + n + 1)//2 -i

            numsi_1 = (-infinity if i==0 else nums1[i-1])
            numsi = (infinity if i==m else nums1[i])
            numsj_1 = (-infinity if j==0 else nums2[j-1])
            numsj = (infinity if j==n else nums2[j])

            if numsi_1 <= numsj:
                median1 = max(numsi_1,numsj_1)
                median2 = min(numsi,numsj)
                l = i+1
            else:
                r = i-1
        return median1 if (m+n)&1 else (median1+median2)/2



# @lc code=end

