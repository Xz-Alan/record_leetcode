#include <iostream>
using namespace std;
#include <string>
#include <algorithm>
class Solution
{
public:
    int maxConsecutiveAnswers(string answerKey, int k)
    {
        return max(find_largest(answerKey, k, 'T'), find_largest(answerKey, k, 'F'));
    }
    int find_largest(const string &answerKey, const int k, char ch)
    {
        int res = 0, left = 0, sum = 0;
        for (int right = 0; right < answerKey.size(); right++)
        {
            sum += answerKey[right] != ch;
            while (sum > k)
            {
                sum -= answerKey[left] != ch;
                left++;
            }
            res = max(res, right - left + 1);
        }
        return res;
    }
};