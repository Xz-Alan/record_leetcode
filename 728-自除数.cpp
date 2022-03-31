#include <iostream>
using namespace std;
#include <vector>
class Solution
{
public:
    vector<int> selfDividingNumbers(int left, int right)
    {
        vector<int> res;
        for (int i = left; i <= right; i++)
        {
            if (isselfDividing(i))
            {
                res.push_back(i);
            }
        }
        return res;
    }
    bool isselfDividing(int num)
    {
        int x = num;
        while (x)
        {
            int d = x % 10;
            if (d == 0 || num % d != 0)
                return false;
            x /= 10;
        }
        return true;
    }
};