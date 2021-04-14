# LeetCode

[toc]

## 题解

#### 26./80. 删除有序数组中的重复项 1/2

双指针：

慢指针指向非重复项

快指针指向数组序列

#### 39.40. 组合总和 1/2

搜索回溯

递归函数`dfs(begin, combine, target)`

`target <= 0`或者`index = 数组的大小`，递归结束

40要求不重复，即加入约束：

```
if index > begin and candidates[index] == candidates[index - 1]:
    continue
```

### 二分

#### 33./81. 搜索旋转排序数组 1/2

旋转 --> 绕某个点旋转

旋转排序数组 --> 部分有序数组 --> 二分查找 --> 比较 左值、中值和右值

有重复元素时影响有序数组的判断，存在`a[l]=a[mid]=a[r]`的情况，需要特殊讨论

### 153./154. 寻找旋转排序数组中的最小值 1/2

旋转 --> 最后一个数到数组第一位，循环旋转

仅比较 **中值和右值**

有重复元素时，存在`a[mid]=a[r]`的情况，需要特殊讨论

### 264. 丑数2

给定整数n，返回第n个丑数

#### 1、优先队列（最小堆）

初始堆为1（最小丑数） --> 取出堆顶元素x并将2$x$，3$x$，5$x$加入堆 --> 避免重复元素 --> 哈希集合Set记录 --> 第 $n$ 次从最小堆中取出的元素即为第 $n$ 个丑数。

#### 2、动态规划（多路归并）（三指针）

定义数组$dp$，其中$dp[i]$表示第$i$个丑数，第$n$个丑数即为$dp[n]$。

定义三个指针$p2$、$p3$、$p5$表示下一个丑数是当前指针指向的丑数乘以对应的质因数。

$dp[i]=min(dp[p2] \times 2, dp[p3] \times 3, dp[p5] \times 5)$，然后分别比较$dp[i]$和$dp[p2], dp[p3], dp[p5]$是否相等，如果相等则将对应的指针加1。

### 179. 最大数

- map() 函数：`map(function, iterable,...)`

  Python 2 返回列表；Python 3 返回迭代器

- sort() 函数：`sort(key=None, reverse=False)`

  key: 具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序

  reverse: 排序规则，reverse = True 降序， reverse = False 升序（默认）

  Python 3中没有cmp，只有key

- `from functools import cmp_to_key` 比较函数

  例如`cmp_to_key(lambda x, y : int(y + x) - int(x + y))`

- `str.join(sequence)`将序列中的元素以指定的字符连接生成一个新的字符串

## 方法总结