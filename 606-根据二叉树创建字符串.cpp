#include <iostream>
using namespace std;
#include <string>
#include <unordered_set>
#include <deque>

// Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    string tree2str(TreeNode *root)
    {
        // 递归
        // if (root == nullptr)
        //     return "";
        // if (root->left == nullptr && root->right == nullptr)
        //     return to_string(root->val);
        // if (root->right == nullptr)
        //     return to_string(root->val) + "(" + tree2str(root->left) + ")";
        // return to_string(root->val) + "(" + tree2str(root->left) + ")(" + tree2str(root->right) + ")";
        // 迭代
        string res = "";
        deque<TreeNode *> que;
        que.push_back(root);
        unordered_set<TreeNode *> vis;
        while (!que.empty())
        {
            TreeNode *cur = que.back();
            if (vis.count(cur))
            {
                if (cur != root)
                    res += ")";
                que.pop_back();
            }
            else
            {
                vis.insert(cur);
                if (cur != root)
                    res += "(";
                res += to_string(cur->val);
                if (!cur->left && cur->right)
                    res += "()";
                if (cur->right)
                    que.push_back(cur->right);
                if (cur->left)
                    que.push_back(cur->left);
            }
        }
        return res;
    }
};