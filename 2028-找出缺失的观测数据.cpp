#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
class Solution
{
public:
    vector<int> missingRolls(vector<int> &rolls, int mean, int n)
    {
        int missingSum = mean * (n + rolls.size());
        for (int &roll : rolls)
        {
            missingSum -= roll;
        }
        if (missingSum < n || missingSum > 6 * n)
        {
            return {};
        }
        int quotient = missingSum / n, remainder = missingSum % n;
        vector<int> missing(n);
        for (int i = 0; i < n; i++)
        {
            missing[i] = quotient + (i < remainder ? 1 : 0);
        }
        return missing;
    }
};