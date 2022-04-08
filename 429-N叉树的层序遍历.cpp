#include <iostream>
using namespace std;
#include <vector>
#include <queue>
// Definition for a Node.
class Node
{
public:
    int val;
    vector<Node *> children;

    Node() {}

    Node(int _val)
    {
        val = _val;
    }

    Node(int _val, vector<Node *> _children)
    {
        val = _val;
        children = _children;
    }
};

class Solution
{
public:
    vector<vector<int>> levelOrder(Node *root)
    {
        queue<Node *> que;
        if (root)
            que.emplace(root);
        vector<vector<int>> result;
        while (!que.empty())
        {
            int sz = que.size();
            vector<int> res;
            for (int i = 0; i < sz; i++)
            {
                Node *cur = que.front();
                que.pop();
                res.push_back(cur->val);
                for (auto &tree : cur->children)
                {
                    que.emplace(tree);
                }
            }
            result.push_back(res);
        }
        return result;
    }
};