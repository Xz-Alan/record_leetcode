#include <iostream>
using namespace std;
class Solution
{
public:
    bool hasAlternatingBits(int n)
    {
        int a = n ^ (n >> 1);
        return (a & (a + 1) == 0);
    }
};