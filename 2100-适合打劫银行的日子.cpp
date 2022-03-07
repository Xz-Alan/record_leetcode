#include <iostream>
using namespace std;
#include <algorithm>
#include <vector>

class Solution
{
public:
    vector<int> goodDaysToRobBank(vector<int> &security, int time)
    {
        int n = security.size();
        vector<int> res;
        // 前缀和
        // if (time == 0)
        // {
        //     for (int i = 0; i < n; i++)
        //     {
        //         res.push_back(i);
        //     }
        //     return res;
        // }
        // int left = 0, right = 0;
        // for (int i = 1; i < n - time; i++)
        // {
        //     if (security[i] <= security[i - 1])
        //     {
        //         left++;
        //     }
        //     else
        //     {
        //         left = 0;
        //     }
        //     if (security[i + time - 1] <= security[i + time])
        //     {
        //         right++;
        //     }
        //     else
        //     {
        //         right = 0;
        //     }
        //     if (left >= time && right >= time)
        //     {
        //         res.push_back(i);
        //     }
        // }
        // 动态规划
        vector<int> left(n), right(n);
        for (int i = 1; i < n; i++)
        {
            if (security[i] <= security[i - 1])
            {
                left[i] = left[i - 1] + 1;
            }
            if (security[n - i - 1] <= security[n - i])
            {
                right[n - i - 1] = right[n - i] + 1;
            }
        }
        for (int i = time; i < n - time; i++)
        {
            if (left[i] >= time && right[i] >= time)
            {
                res.push_back(i);
            }
        }
        return res;
    }
};

int main()
{
    vector<int> security = {5, 3, 3, 3, 5, 6, 2};
    int time = 2;
    Solution sol;
    vector<int> res = sol.goodDaysToRobBank(security, time);
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << " ";
    }
    cout << endl;
}