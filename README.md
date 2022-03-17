

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

### 53. 最大子序和363. 矩形区域不超过k的最大数值和

#### 1) 动态规划

`f(i)=max{f(i−1) + nums[i], nums[i]}`

#### 2) 前缀和

根据`sum(i,j) = sum(0,j) - sum(0,i)`

记录当前综合`cur_sum`和前`i`总和的最小值`min_sum`即可

### 363. 矩形区域不超过k的最大数值和

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

### 198. 打家劫舍

动态规划

转移方程：`dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])`

边界条件：`dp[0] = nums[0]` & ` dp[1] = max(nums[0], nums[1])`

进阶：固定数组dp --> 滚动数组，只存储前两个值

`first, second = second, max(nums[i] + first, second)`

### 740. 删除与获得点数

记元素$x$在数组中出现的次数为 $c_x$，可以用一个数组$\textit{sum}$记录数组$\textit{nums}$中所有相同元素之和，即$\textit{sum}[x]=x \cdot c_x$。

对$\textit{sum}$运用[198. 打家劫舍](###198. 打家劫舍)动态规划的方法进行计算

### 690. 员工的重要性

深度/广度优先搜索

调试：

```
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def genEmployee(employees):
    size = len(employees)
    emps = []
    for i in range(size):
        emps.append(Employee(0,0,[]))
        emps[i].id = employees[i][0]
        emps[i].importance = employees[i][1]
        emps[i].subordinates = employees[i][2]
    return emps
    
employees = genEmployee([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]])
```

### 872. 叶子相似的数

深度优先搜索，先搜索当前节点的左子节点，再搜索当前节点的右子节点。

### 1723. 完成所有工作的最短时间

二分+递归回溯+剪枝

[1011. 在*D*天内送达包裹的能力](###1011. 在*D*天内送达包裹的能力) + [698. 划分为k个相等的子集](###698. 划分为k个相等的子集) 综合题解

二分模板：

```python
left, right = 最小值, 最大值
while  left < right:
    limit = (left + right)//2
    if 工作可以分完(limit):
        right = limit
    else:
        left = limit + 1
return left
```

判断工作是否可以分完，参考[698. 划分为k个相等的子集](###698. 划分为k个相等的子集)的暴力回溯递归。

### 698. 划分为k个相等的子集

暴力回溯递归...

细节优化：

1. `if(groups[i] == 0): break` --> 一票否决：如果有某一个数字无法与其他数字“凑成对”，则直接False；
2. `nums.sort()` --> 对数组进行排序，先放置较大元素。

### 29. 两数相除

### 13. 罗马数字转整数

字典：7个字母对应7个数值。

当前字符值小于其右边字符值，则减去该值，否则加上该值。

### 2. 两数相加

链表逆序相加，模拟实现即可。

> 连等赋值的逻辑顺序

```
curr.next = curr = ListNode(val)
# 等价于
# curr.next = ListNode(val)
# curr = curr.next
```

链表调试

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def genListNode(arr):
    def gen(arr, i):
        if i < len(arr):
            ln = ListNode(arr[i])
            ln.next = gen(arr, i + 1)
            return ln
    return gen(arr, 0)
```

### 1734. 解码异或后的排列

> `perm` 是前 `n` 个正整数的排列，且 `n` 是个 **奇数**

按照[740. 删除与获得点数](###740. 删除与获得点数)的方法，需要求出perm的第一个值`perm[0]`

因为`perm[0] = total ^ odd`，且有：

`total = 1 ^ 2 ^ ···^ n = perm[0] ^ perm[1] ^ ··· ^ perm[n-1]`

`odd = encoded[1] ^ encoded[3] ^ ··· ^ encoded[n-2] = perm[1] ^ perm[2] ^ ··· ^ perm[n-1] `

即可计算出`perm[0]`，进一步得到`perm`。

### 1269. 停在原地的方案数

动态规划：`dp[i][j]`表示在`i`步操作后，指针位于小标`j`的方案数。

状态转移方程：`dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1] `

初始状态：`dp[0][0] = 1`

取值范围：`0 <= i <= steps`&`0 <= j <= min(arrLen - 1, steps)`

### 1442. 形成两个异或相等数组的三元组数组

1. i到k的连续异或等于0即可
2. 前缀和yyds（异或常用套路）

`s[]`为前缀和，则`s[i] == s[k + 1]`中的所有`j`均符合，即`count += k - i`

3. 优化：哈希表 -->遍历`k`时，找到所有符合要求的`i`，记录两个哈希表：

- 下标`i`出现的次数`m`
- 下标`i`之和`total`

即有：`count = m * k - total `

### 692. 前k个高频单词

1. `Count()`频次计数
2. `cmp_to_key`排序输出前k高频

```
def topKFrequent(self, words: List[str], k: int) -> List[str]:
	d = Counter(words)
	return sorted(d.keys(), key=cmp_to_key(lambda x, y: int(d[x] < d[y] or (d[x] == d[y] and x > y)) - 0.5))[:k]
```

### 1035. 不相交的线（马甲）和1143. 最大公共子序列

二维动态规划：`dp[i][j]`表示`nums1[0:i]`和`nums2[0:j]`的最长公共子序列的长度

初始状态：`dp[0][j] = 0 & dp[i][0] = 0`

状态转移：$d p[i][j]=\left\{\begin{array}{ll}dp[i-1][j-1]+1, & nums_1[i-1]=nums_2[j-1] \\ \max (dp[i-1][j], dp[i][j-1]), & nums_1[i-1] =nums_2[j-1]\end{array}\right.$

### 664. 奇怪的打印机

二维动态规划：`dp[i][j]`表示打印完成字符串`s`区间`[i,j]`的最少操作数

初始状态：`dp[i][i] = 1`

状态转移：$dp[i][j]=\left\{\begin{array}{ll}dp[i][j-1], & s[i]=s[j] \\ \min_{k=i}^{j=1} dp[i][k]+dp[k+1][j], & s[i] \neq s[j]\end{array}\right.$

### 1190. 反转每对括号间的子串

>输入：s = "(ed(et(oc))el)"
>
>输出："leetcode"

从左到右遍历字符串，记录字母到str

遇左括号，将str插入到栈中，并将str置空，进入下一层

遇右括号，将str反转并返回到上一层

### 461. 汉明距离和477. 汉明距离总和

移位统计，所有元素二进制的第`i`位共有`c`个**1**，`n - c`个**0**，则这些元素在二进制的第`i`位上的汉明距离之和为

`c * (n - c)`。

### 1744. 你能在你最喜欢的那天吃到最喜欢的糖果吗？

前缀和

```python
from itertools import accumulate    # 前缀和
import operator
_sum = list(accumulate(candiesCount))
```

两个区间`[x1,y1]`和`[x2,y2]`求交集 --> `not(x1 > y2 or y1 < x2)`

### 494. 目标和

动态规划

记数组的元素和为`sum`，添加 `-`号的元素之和为`neg`，则其余添加`+`的元素之和为`sum - neg`，则有：

`(sum - neg) - neg = sum - 2 * neg = target` --> `neg = (sum - target) / 2`

`dp[i][j]`表示在数组`nums`的前`i`个数中选取元素，使得这些元素之和等于`j`的方案数。最终目标为`dp[n][neg]`

边界条件：$d p[0][j]=\left\{\begin{array}{ll}1, & j=0 \\ 0, & j \geq 1\end{array}\right.$

状态转移方程：$d p[i][j]=\left\{\begin{array}{ll}d p[i-1][j], & j<n u m s[i] \\ d p[i-1][j]+d p[i-1][j-n u m s[i]], & j \geq n u m s[i]\end{array}\right.$

###  89. 格雷编码

二进制数转格雷码
$$
g(i)=b(i) \oplus b(i+1)
$$

### [2104. 子数组范围和](https://leetcode-cn.com/problems/sum-of-subarray-ranges/)

**思路**

1. 暴力-两层遍历：从左向右更新最大最小元素；
2. 单调栈

![image-20220304172604376](https://s2.loli.net/2022/03/04/NjuWPfGecqv7Jz9.png)

> 1. 单调递增栈，分别得到左侧最近的比num小的数，右侧最近的比num小的数；
> 2. 单调递减栈，分别得到左侧最近的比num大的数，右侧最近的比num大的数。

```python
# 单调递增栈
while min_stack and num < nums[min_stack[-1]]:
    min_stack.pop()
min_l[i] = min_stack[-1] if min_stack else -1
min_stack.append(i)
# 单调递减栈
while max_stack and num >= nums[max_stack[-1]]:
    max_stack.pop()
max_l[i] = max_stack[-1] if max_stack else -1
max_stack.append(i)
```



### [521. 最长特殊序列 Ⅰ](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/)

**思路**

阅读理解题，字符串相同返回-1，不同比较字符串长度。

### [--2100. 适合打劫银行的日子--](https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank/)

**思路**

1. 前缀和
2. 动态规划

记录第$i$天前连续非递增的天数$left[i]$ 和 第$i$天后连续非递减的天数$right[i]$。

**题解**

```python
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # 前缀和
        # if time > 2 * len(security) + 1:
        #     return []
        # if time == 0:
        #     return list(range(len(security)))
        # res = []
        # left = right = 0
        # for i in range(1, len(security) - time):
        #     if security[i] <= security[i-1]:
        #         left += 1
        #     else:
        #         left = 0
        #     if security[i+time-1] <= security[i+time]:
        #         right += 1
        #     else:
        #         right = 0
        #     if left >= time and right >= time:
        #         res.append(i)
        # return res
        # 动态规划
        n = len(security)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if security[i] <= security[i-1]:
                left[i] = left[i-1] + 1
            if security[n-i-1] <= security[n-i]:
                right[n-i-1] = right[n-i] + 1
        return [i for i in range(time, n-time) if left[i] >= time and right[i] >= time]
```

### [504. 七进制数](https://leetcode-cn.com/problems/base-7/)

**思路**：从最低位到最高位还原七进制的值为`num%7`。当输入为负，我们可以先取`num`的绝对值来求七进制，最后再添加负号。

**题解**

```
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        res = []
        num = abs(num)
        while num:
            res.append(str(num % 7))
            num //= 7
        if negative:
            res.append('-')
        return "".join(reversed(res))
```

### [2055. 蜡烛之间的盘子](https://leetcode-cn.com/problems/plates-between-candles/)

**思路**：对于子字符串`[left,right]`，找到`left`右侧最近的蜡烛位置和`right`左侧最近的蜡烛位置，则这之间的所有盘子均为有效盘子。因此对于每一个下标，维护三个数组：`left[n]`、`right[n]`、`presum[n]`，其中前缀和用于计算子区间的有效盘子。

### [798. 得分最高的最小轮调](https://leetcode-cn.com/problems/smallest-rotation-with-highest-score/)

**思路**：针对数组中的每一个数，找到所有能够“加分”的k值，可以发现，实际上满足条件的k值是一个范围`[i+1, n-nums[i]+i]`，并对区间内所有数取`(mod)n`，接着找到所有满足条件的k值出现的次数最大值即可。

但该方法时间复杂度为`O(n^2)`，超出时间范围，因此采用**差分数组**的思想，本质上为前缀和的逆过程。遍历数组`nums`的所有元素并更新差分数组之后，遍历数组`diffs`并计算前缀和，则每个下标处的前缀和表示当前论调下标处的得分，遍历结束之后得到结果。

差分数组`diffs`有：$diffs[i] = count[i]-count[i-1]$，因此在遍历数组`nums`时，令`low = (i+1) mod n`，令`high = (i-nums[i]+n-1) mod n`，将`diffs[low]`的值加1，将`diffs[high]`的值减1，如果`low>=high`，则将`diffs[0]`的值加1。

```
for i in range(n):
    low = (i+1) % n
    high = (n-nums[i]+i+1) % n
    diffs[low] += 1
    diffs[high] -= 1
    if low >= high:
        diffs[0] += 1
```

### [589. N 叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)

**思路**：采用二叉树前序遍历的深度优先搜索的模板，按照根-->左-->右的顺序，改为根-->N子节点的顺序，对每个父节点的children节点进行遍历即可。



### [590. N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)

**思路**：采用二叉树后序遍历的深度优先搜索的模板，按照左-->右-->根的顺序，改为N子节点-->根的顺序，对每个父节点的children节点进行遍历即可。

### [2044. 统计按位或能得到最大值的子集数目](https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets/)

**思路**：用`n`比特数表示`2^n`个子集，第`i`位表示数组第`i`个元素的选取状态，通过移位来判断第`j`个元素是否被选取。

**题解**

```python
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val, res, n = 0, 0, len(nums)
        for i in range(1 << n):
            # 用n比特数表示2^n个子集，第i位表示数组第i个元素的选取状态
            tmp = 0
            for j in range(n):
                # 通过移位来判断第j个元素是否被选取
                if (i >> j) & 1 == 1:
                    tmp |= nums[j]
            if tmp == max_val:
                res += 1
            elif tmp > max_val:
                max_val = tmp
                res = 1
        return res
```

### [720. 词典中最长的单词](https://leetcode-cn.com/problems/longest-word-in-dictionary/)

**思路**

1. 先对数组`words`排序，按照长度升序、字典降序的顺序排序，因为所有单词都由其他单词逐步添加一个字母组成，构建哈希表加入符合条件的单词，对排序后的`words`遍历一遍即可得到答案。
2. TODO：字典树(Trie(前缀树))。

**注意**：对于python排序时，因为str不能取负, 因此先长度降序，字典升序，再反转。

>*words*.sort(*key*=*lambda* *x*: (-len(*x*), *x*), *reverse*=True)

**题解**

```c++
class Solution
{
public:
    string longestWord(vector<string> &words)
    {
        string res = "";
        unordered_set<string> hash;
        hash.emplace(res);
        sort(words.begin(), words.end(), [](const string &a, const string &b)
             {
                 if (a.size() != b.size())
                 {
                     return a.size() < b.size(); // 长度升序
                 }
                 else
                 {
                     return a > b; // 字典降序
                 }
             });
        for (auto &word : words)
        {
            if (hash.count(word.substr(0, word.size() - 1)))
            {
                res = word;
                hash.emplace(word);
            }
        }
        return res;
    }
};
```



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

#### 二叉树遍历

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

#### 莫里斯遍历

#### N叉树遍历

### 二分查找

