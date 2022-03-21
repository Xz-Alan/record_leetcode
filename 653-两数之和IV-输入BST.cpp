#include <iostream>
using namespace std;
#include <string>
#include <unordered_set>
#include <deque>
#include <stack>
#include <queue>

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
    unordered_set<int> hashset;
    bool findTarget(TreeNode *root, int k)
    {
        // DFS+哈希
        // if (!root)
        //     return false;
        // if (hashset.count(k - root->val))
        //     return true;
        // hashset.insert(root->val);
        // return findTarget(root->left, k) || findTarget(root->right, k);
        // BFS+哈希
        queue<TreeNode *> que;
        que.push(root);
        while (!que.empty())
        {
            TreeNode *cur = que.front();
            que.pop();
            if (hashset.count(k - cur->val))
                return true;
            hashset.insert(cur->val);
            if (cur->left)
                que.push(cur->left);
            if (cur->right)
                que.push(cur->right);
        }
        return false;
    }
};