#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        '''
        # 枚举时针和分针
        for hour in range(12):
            for mins in range(60):
                if bin(hour).count("1") + bin(mins).count("1") == turnedOn:
                    ans.append(f"{hour}:{mins:02d}")
        '''
        # 二进制枚举
        for i in range(1024):
            hour, mins = i >> 6, i & 0x3f   # 位运算取出高 4 位和低 6 位
            if hour < 12 and mins < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{hour}:{mins:02d}")
        return ans
# @lc code=end

