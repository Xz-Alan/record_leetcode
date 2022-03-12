#include <iostream>
using namespace std;
#include <vector>

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
    void dfs(const Node *cur, vector<int> &res)
    {
        if (cur == nullptr)
        {
            return;
        }
        res.push_back(cur->val);
        for (auto &tree : cur->children)
        {
            dfs(tree, res);
        }
    }
    vector<int> preorder(Node *root)
    {
        vector<int> res;
        dfs(root, res);
        return res;
    }
};
