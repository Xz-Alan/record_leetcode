#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <numeric>
class Solution
{
public:
    int calPoints(vector<string> &ops)
    {
        vector<int> res;
        for (auto &ch : ops)
        {
            int n = res.size();
            switch (ch[0])
            {
            case '+':
                res.push_back(res[n - 1] + res[n - 2]);
                break;
            case 'D':
                res.push_back(2 * res[n - 1]);
                break;
            case 'C':
                res.pop_back();
                break;
            default:
                res.push_back(stoi(ch));
                break;
            }
        }
        return accumulate(res.begin(), res.end(), 0);
    }
};