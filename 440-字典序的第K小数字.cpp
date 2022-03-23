#include <iostream>
using namespace std;
#include <algorithm>

class Solution
{
public:
    int getStep(long n, int cur)
    {
        int step = 0;
        // 注意取值范围
        long first = cur, last = cur;
        while (first <= n)
        {
            step += min(n, last) - first + 1;
            first *= 10;
            last = last * 10 + 9;
        }
        return step;
    }
    int findKthNumber(int n, int k)
    {
        int cur = 1;
        k--;
        while (k)
        {
            int step = getStep(n, cur);
            if (step <= k)
            {
                k -= step;
                cur++;
            }
            else
            {
                k--;
                cur *= 10;
            }
        }
        return cur;
    }
};