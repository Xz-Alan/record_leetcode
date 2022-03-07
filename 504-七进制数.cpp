#include <iostream>
using namespace std;
#include <algorithm>
#include <string>

class Solution
{
public:
    string convertToBase7(int num)
    {
        if (num == 0)
        {
            return "0";
        }
        bool negative = num < 0;
        num = abs(num);
        string res;
        while (num > 0)
        {
            res.push_back((num % 7) + '0');
            num /= 7;
        }
        if (negative)
        {
            res.push_back('-');
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

int main()
{
    int num = 100;
    Solution sol;
    string res = sol.convertToBase7(num);
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << ' ';
    }
    cout << endl;
}