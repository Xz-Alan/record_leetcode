#include <iostream>
using namespace std;
class Solution
{
public:
    int trailingZeroes(int n)
    {
        int res = 0; // = n/5+n/25+n/125+n/625+n/3125;
        while (n)
        {
            n /= 5;
            res += n;
        }
        return res;
    }
};