# LeetCode

[toc]

## 题解

### 26./80. 删除有序数组中的重复项 1/2

双指针：

慢指针指向非重复项

快指针指向数组序列

### 39.40. 组合总和 1/2

搜索回溯

递归函数`dfs(begin, combine, target)`

`target <= 0`或者`index = 数组的大小`，递归结束

40要求不重复，即加入约束：

```
if index > begin and candidates[index] == candidates[index - 1]:
    continue
```

### 33./81. 搜索旋转排序数组 1/2

旋转 --> 绕某个点旋转

旋转排序数组 --> 部分有序数组 --> 二分查找 --> 比较 左值、中值和右值

有重复元素时影响有序数组的判断，存在`a[l]=a[mid]=a[r]`的情况，需要特殊讨论

### 153./154. 寻找旋转排序数组中的最小值 1/2

旋转 --> 最后一个数到数组第一位，循环旋转

仅比较 **中值和右值**

有重复元素时，存在`a[mid]=a[r]`的情况，需要特殊讨论

### 264. 丑数2

给定整数n，返回第n个丑数

#### 1) 优先队列（最小堆）

初始堆为1（最小丑数） --> 取出堆顶元素x并将2$x$，3$x$，5$x$加入堆 --> 避免重复元素 --> 哈希集合Set记录 --> 第 $n$ 次从最小堆中取出的元素即为第 $n$ 个丑数。

#### 2) 动态规划（多路归并）（三指针）

定义数组$dp$，其中$dp[i]$表示第$i$个丑数，第$n$个丑数即为$dp[n]$。

定义三个指针$p2$、$p3$、$p5$表示下一个丑数是当前指针指向的丑数乘以对应的质因数。

$dp[i]=min(dp[p2] \times 2, dp[p3] \times 3, dp[p5] \times 5)$，然后分别比较$dp[i]$和$dp[p2], dp[p3], dp[p5]$是否相等，如果相等则将对应的指针加1。

### 179. 最大数

- map() 函数：`map(function, iterable,...)`

  Python 2 返回列表；Python 3 返回迭代器

- sort() 函数：`sort(key=None, reverse=False)`

  key: 具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序

  reverse: 排序规则，reverse = True 降序， reverse = False 升序（默认）

  Python 3中没有cmp，只有key

- `from functools import cmp_to_key` 比较函数

  例如`cmp_to_key(lambda x, y : int(y + x) - int(x + y))`

- `str.join(sequence)`将序列中的元素以指定的字符连接生成一个新的字符串

### 220. 存在重复元素3

#### 1) 滑动窗口

按照题目要求，需要在滑窗`abs(i - j) <= k`中找到满足`abs(nums[i] - nums[j]) <= t`的元素

直接遍历会超时 --> 内部有序的数据结构

`from sortedcontainers import SortedList`

通过二分查找，快速查询到**小于等于u的最大值**和**大于等于u的最小值**，即**有序集合中最接近u的值**

滑窗不断右移，完成遍历

#### 2) 桶排序



### 91. 解码方法

动态规划 --> `f[i]`表示字符串`s`的前`i`个字符的解码方法数。

初始状态：`f[0]=1`

状态转移：

- $s[i] \ne 0$ 时，`f[i] += f[i-1]`
- $s[i-1] \ne 0 $ and $ 10 \cdot s[i-1] + s[i] \le 26$ 时，`f[i] += f[i-2]`

### 53. 最大子序和363.矩形区域不超过k的最大数值和

#### 1) 动态规划

`f(i)=max{f(i−1) + nums[i], nums[i]}`

#### 2) 前缀和

根据`sum(i,j) = sum(0,j) - sum(0,i)`

记录当前综合`cur_sum`和前`i`总和的最小值`min_sum`即可

### 363.矩形区域不超过k的最大数值和

固定左右边界，枚举前缀和

优化 --> `from sortedcontainers import SortedList` 有序集合，二分查找不超过k的最大数值和

### 368. 最大整除子集

#### 1) 动态规划

1. 动态规划找出最大子集的个数、最大子集中的最大整数

`dp[i]`表示以`nums[i]`为最大整数的最大子集的个数

状态转移方程：

```python
for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[i] % nums[j] == 0:
            dp[i] = max(dp[i], dp[j] + 1)
```

2. 倒推获得最大子集输出

#### 2) 字典dp

`dp = dict{}`，记录最大子集的个数的同时，记录子集输出

### 1011. 在*D*天内送达包裹的能力

贪心加二分查找

查找运载能力，左边界为`max(weights)`，右边界为`sum(weights)`

贪心得到运载天数确定二分判定条件

### 136. 只出现一次的数字

异或：

1. 任何数和 0 做异或运算，结果仍然是原来的数，即 $a \oplus 0 = a$。
2. 任何数和其自身做异或运算，结果是 0，即$a \oplus a = 0$。
3. 异或运算满足交换律和结合律，即$a \oplus b \oplus a=b \oplus a \oplus a=b \oplus (a \oplus a)=b \oplus 0 = b$。

因此，只出现一次的数字 = 数组全部元素的异或运算结果

```python
def singleNumber(self, nums: List[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)
```

### 1720. 解码异或后的数组

已知$encoded[i−1] = arr[i−1] \oplus arr[i]$，$arr[0]=first$，则有：

$arr[i]=arr[i−1] \oplus encoded[i−1]$。

## 方法总结

### 二叉树

#### 数组创建二叉树作调试用

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def genTree(arr):
    def gen(arr, i):
        if i < len(arr):
            tn = TreeNode(arr[i]) if arr[i] is not None else None
            if tn is not None:
                tn.left = gen(arr, 2 * i + 1)
                tn.right = gen(arr, 2 * i + 2)
            return tn
    return gen(arr, 0)

root = genTree(arr)
```

#### 遍历

- 前序： 根-->左-->右
- 中序：左-->根-->右
- 后序：左-->右-->根

##### 递归遍历

```python
from typing import List
class Solution_1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序递归
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # 中序递归
        return self.preorderTraversal(root.left) + [root.val] + self.preorderTraversal(root.right)
        # 后序递归
        # return self.preorderTraversal(root.left) + self.preorderTraversal(root.right) + [root.val]
      	
class Solution_2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return
            # 前序递归
            # res.append(cur.val)
            # dfs(cur.left)
            # dfs(cur.right)
            # 中序递归
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)
            # 后序递归
            # dfs(cur.left)
            # dfs(cur.right)
            # res.append(cur.val)
            
        res = []
        dfs(root)
        return res
```

##### 迭代遍历

```python
# 只需一个栈的空间
class Solution_1:
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        
        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res
        
        # # 后序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]
        

# 标记法迭代（需要双倍的空间来存储访问状态）0表示当前未访问，1表示已访问。
class Solution_2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(0, root)]
        while stack:
            flag, cur = stack.pop()
            if not cur: continue
            if flag == 0:
                # 前序，标记法
                stack.append((0, cur.right))
                stack.append((0, cur.left))
                stack.append((1, cur))
                
                # # 后序，标记法
                # stack.append((1, cur))
                # stack.append((0, cur.right))
                # stack.append((0, cur.left))
                
                # # 中序，标记法
                # stack.append((0, cur.right))
                # stack.append((1, cur))
                # stack.append((0, cur.left))  
            else:
                res.append(cur.val)  
        return res
        
        # # 层序，标记法
        # res = []
        # queue = [(0, root)]
        # while queue:
        #     flag, cur = queue.pop(0)  # 注意是队列，先进先出
        #     if not cur: continue
        #     if flag == 0:
                  # 层序遍历这三个的顺序无所谓，因为是队列，只弹出队首元素
        #         queue.append((1, cur))
        #         queue.append((0, cur.left))
        #         queue.append((0, cur.right))
        #     else:
        #         res.append(cur.val)
        # return res
```

##### 莫里斯遍历

##### N叉树遍历

### 二分查找



