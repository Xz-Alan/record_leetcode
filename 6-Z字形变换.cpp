#include <iostream>
using namespace std;
#include <string>

class Solution
{
public:
    string convert(string s, int numRows)
    {
        int n = s.size();
        int r = numRows;
        if (r == 1 || r >= n)
        {
            return s;
        }
        int t = 2 * r - 2;
        string res;
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < n - i; j += t)
            {
                res.push_back(s[j + i]);
                if (0 < i && i < r - 1 && j + t - i < n)
                {
                    res.push_back(s[j + t - i]);
                }
            }
        }
        return res;
    }
};

int main()
{
    string s = "PAYPALISHIRING";
    int numRows = 3;
    Solution sol;
    string res = sol.convert(s, numRows);
    cout << res << endl;
}