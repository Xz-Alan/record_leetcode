[toc]

# LeetCode

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

### [2043. 简易银行系统](https://leetcode-cn.com/problems/simple-bank-system/)

纯模拟

### [606. 根据二叉树创建字符串](https://leetcode-cn.com/problems/construct-string-from-binary-tree/)

**思路**

1. 递归实现
2. 迭代实现

**迭代题解**

```python
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        stack = [root]
        vis = set()
        while stack:
            cur = stack[-1]
            if cur in vis:
                if cur != root:
                    res += ")"
                stack.pop()
            else:
                vis.add(cur)
                if cur != root:
                    res += "("
                res += str(cur.val)
                if not cur.left and cur.right:
                    res += "()"
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return res
```

### [653. 两数之和 IV - 输入 BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)

**思路**

1. BST中序遍历后为升序数组，转化为双指针找两数之和的问题；
2. 通过DFS或BFS遍历BST，用哈希表记录遍历过的节点，如果存在`k-x`，即返回`True`。

### [2038. 如果相邻两个颜色均相同则删除当前颜色](https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/)

**思路**

分别记录Alice和Bob操作的次数：`A`或`B`连续出现3次及以上的次数，返回`num_a>num_b`。

### [440. 字典序的第K小数字](https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/)

**思路**

比较暴力的思路是把所有的数字转换成字符串，然后排序找到第`k`小的数字即可，显然不满足时间复杂度要求。

引入**字典树**，将所有小于等于`n`的数字按照字典序的方式进行重建，前序遍历即可得到字典序从小到大的数字序列。字典树示意图如下：

<img src="https://s2.loli.net/2022/03/23/GQ3qMVW1tlhOoKY.png" alt="image-20220323125628958" style="zoom:80%;" />

设当前字典树第$i$小的节点为$n_i$，设以$n_i$为根节点构成的子树的节点数目为$step(n_i)$，则有：

<img src="https://s2.loli.net/2022/03/23/NxCIX7AmbctY91y.png" alt="image-20220323130038152" style="zoom:80%;" />

对于$step(n_i)$，按照层次遍历子树，$\textit{first}_i$指向第$i$层的最左侧的孩子节点，$\textit{last}_i$指向第$i$层的最右侧的孩子节点，则有$\textit{first}_i=10\times\textit{first}_{i-1}$，$\textit{last}_i=10\times\textit{last}_{i-1}+9$，$step(n_i)=min(n,last_i)-first_i+1$，不断迭代直到$\textit{first}_i > n$则终止向下搜索。

### [661. 图片平滑器](https://leetcode-cn.com/problems/image-smoother/)

**思路**：直接模拟遍历，求$3 \times 3$过滤器的平均值即可，注意角、边、正常情况可以用统一的`[max(i-1,0):min(i+2,h)]`和`[max(j-1,0):min(j+2,w)]`来实现。

### [172. 阶乘后的零](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)

**思路**：`n!`尾零的数量即为因子10的个数，即求质因子2的个数和质因子5的个数的较小值，但质因子5的个数不会大于质因子2的个数，即求`n!`中质因子**5**的个数。

可以通过不断将`n`除以`5`，并累加每次除后的`n`，来得到答案。

### [682. 棒球比赛](https://leetcode-cn.com/problems/baseball-game/)

**思路**：直接模拟

### [2028. 找出缺失的观测数据](https://leetcode-cn.com/problems/find-missing-observations/)

**思路**：简单模拟

### [693. 交替位二进制数](https://leetcode-cn.com/problems/binary-number-with-alternating-bits/)

**思路**：

1. 直接模拟；
2. 位运算：如果`n`的二进制表示总是0、1交替，则有`a=n^(n>>1)`的二进制表示全为一，等价于`a&(a+1)==0`。

### [2024. 考试的最大困扰度](https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam/)

**思路**：滑动窗口，使窗口内异常值出现的次数`<=k`，记录窗口的最大长度。对于本题，求`max(find_largest('T'), find_largest('F'))`。

同[1004. 最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii/)

### [728. 自除数](https://leetcode-cn.com/problems/self-dividing-numbers/)

**思路**：直接遍历判断`[left,right]`的数是否为**自除数**。

注意要求一个数`num`的每一位的值，则有：

```
# python
x = num
while x:
	x, d = divmod(x, 10)
// c++
int x = num;
while (x)
{
    int d = x % 10;
    x /= 10;
}
```

### [954. 二倍数对数组](https://leetcode-cn.com/problems/array-of-doubled-pairs/)

**思路**：

1. 按照绝对值从大到小直接排序，遍历`arr`，找到一个`2*num==match[0]`，则有`match.pop[0]`，否则`match.append(num)`，最终返回`match`的长度不为零。
2. 哈希表排序，首先对`arr`计数器计数，然后按照键绝对值排序，能够对重复元素进行匹配，最坏的时间和空间复杂度同方法1。















