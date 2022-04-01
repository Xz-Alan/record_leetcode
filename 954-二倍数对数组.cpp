#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
#include <unordered_map>
class Solution
{
public:
    bool canReorderDoubled(vector<int> &arr)
    {
        unordered_map<int, int> cnt;
        for (int num : arr)
            cnt[num]++;
        if (cnt[0] % 2)
            return false;
        vector<int> vals;
        for (auto &[x, _] : cnt)
            vals.push_back(x);
        sort(vals.begin(), vals.end(), [](const int a, const int b)
             { return abs(a) < abs(b); });
        for (int x : vals)
        {
            if (cnt[2 * x] < cnt[x])
                return false;
            cnt[2 * x] -= cnt[x];
        }
        return true;
    }
};