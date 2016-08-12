/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        recursive(root);
        return output;
    }

    void recursive(TreeNode* root){
        if (root){
            recursive(root->left);
            recursive(root->right);
            output.push_back(root->val);
        }
    }

    vector<int> output;
};