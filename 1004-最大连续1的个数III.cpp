#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
class Solution
{
public:
    int longestOnes(vector<int> &nums, int k)
    {
        int res = 0, left = 0, sum = 0;
        for (int right = 0; right < nums.size(); right++)
        {
            sum += nums[right] != 1;
            while (sum > k)
            {
                sum -= nums[left] != 1;
                left++;
            }
            res = max(res, right - left + 1);
        }
        return res;
    }
};