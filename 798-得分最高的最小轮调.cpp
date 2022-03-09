#include <iostream>
using namespace std;
#include <vector>
class Solution
{
public:
    int bestRotation(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> diffs(n);
        for (int i = 0; i < n; i++)
        {
            int low = (i + 1) % n;
            int high = (n - nums[i] + i + 1) % n;
            diffs[low]++;
            diffs[high]--;
            if (low >= high)
            {
                diffs[0]++;
            }
        }
        int max_count = 0, count = 0, idx = 0;
        for (int i = 0; i < n; i++)
        {
            count += diffs[i];
            if (count > max_count)
            {
                idx = i;
                max_count = count;
            }
        }
        return idx;
    }
};