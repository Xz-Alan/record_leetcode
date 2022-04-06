#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>
class Solution
{
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges)
    {
        if (n == 1)
            return {0};
        vector<int> degree(n);
        unordered_map<int, vector<int>> map;
        for (auto &edge : edges)
        {
            degree[edge[0]]++;
            degree[edge[1]]++;
            map[edge[0]].push_back(edge[1]);
            map[edge[1]].push_back(edge[0]);
        }
        queue<int> que;
        for (int i = 0; i < n; i++)
        {
            if (degree[i] == 1)
                que.emplace(i);
        }
        vector<int> res;
        while (!que.empty())
        {
            res.clear();
            int length = que.size();
            for (int i = 0; i < length; i++)
            {
                int cur = que.front();
                que.pop();
                res.push_back(cur);
                vector<int> neighbors = map[cur];
                for (int neighbor : neighbors)
                {
                    degree[neighbor]--;
                    if (degree[neighbor] == 1)
                        que.emplace(neighbor);
                }
            }
        }
        return res;
    }
};