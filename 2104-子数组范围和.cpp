#include <iostream>
using namespace std;
#include <algorithm>
#include <vector>
#include <stack>

class Solution
{
public:
    long long subArrayRanges(vector<int> &nums)
    {
        // 暴力
        // long long res = 0;
        // for (int i = 0; i < nums.size(); i++)
        // {
        //     int min_v = INT_MAX;
        //     int max_v = INT_MIN;
        //     for (int j = i; j < nums.size(); j++)
        //     {
        //         min_v = min(min_v, nums[j]);
        //         max_v = max(max_v, nums[j]);
        //         res += max_v - min_v;
        //     }
        // }
        // return res;
        // 单调栈
        int n = nums.size();
        vector<int> min_l(n), min_r(n), max_l(n), max_r(n);
        stack<int> min_stack, max_stack;
        for (int i = 0; i < n; i++)
        {
            int num = nums[i];
            while (!min_stack.empty() && num < nums[min_stack.top()])
            {
                min_stack.pop();
            }
            min_l[i] = min_stack.empty() ? -1 : min_stack.top();
            min_stack.push(i);
            while (!max_stack.empty() && num >= nums[max_stack.top()])
            {
                max_stack.pop();
            }
            max_l[i] = max_stack.empty() ? -1 : max_stack.top();
            max_stack.push(i);
        }
        min_stack = stack<int>();
        max_stack = stack<int>();
        for (int i = n - 1; i >= 0; i--)
        {
            int num = nums[i];
            while (!min_stack.empty() && num <= nums[min_stack.top()])
            {
                min_stack.pop();
            }
            min_r[i] = min_stack.empty() ? n : min_stack.top();
            min_stack.push(i);
            while (!max_stack.empty() && num > nums[max_stack.top()])
            {
                max_stack.pop();
            }
            max_r[i] = max_stack.empty() ? n : max_stack.top();
            max_stack.push(i);
        }
        long long min_sum = 0, max_sum = 0;
        for (int i = 0; i < n; i++)
        {
            int num = nums[i];
            min_sum += (long long)(i - min_l[i]) * (min_r[i] - i) * num;
            max_sum += (long long)(i - max_l[i]) * (max_r[i] - i) * num;
        }
        return max_sum - min_sum;
    }
};

int main()
{
    vector<int> nums = {4, -2, -3, 4, 1};
    Solution sol;
    long long res = sol.subArrayRanges(nums);
    cout << res << endl;
}