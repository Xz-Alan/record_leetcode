#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

class Solution
{
public:
    string longestWord(vector<string> &words)
    {
        string res = "";
        unordered_set<string> hash;
        hash.emplace(res);
        sort(words.begin(), words.end(), [](const string &a, const string &b)
             {
                 if (a.size() != b.size())
                 {
                     return a.size() < b.size(); // 长度升序
                 }
                 else
                 {
                     return a > b; // 字典降序
                 }
             });
        for (auto &word : words)
        {
            if (hash.count(word.substr(0, word.size() - 1)))
            {
                res = word;
                hash.emplace(word);
            }
        }
        return res;
    }
};