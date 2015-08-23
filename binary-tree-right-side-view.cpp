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
    vector<int> output;

    vector<int> rightSideView(TreeNode* root){

        helper(root, 0);
        return this->output;
    }

    int helper(TreeNode* root, int level){
        if (!root){
            return 0;
        }
        if (level == output.size()){
            this->output.push_back(root->val);
        }
        helper(root->right, level + 1);
        helper(root->left, level + 1);
    }



    vector<int> rightSideViewIterative(TreeNode* root) {
        vector<int> output;
        vector<tuple<TreeNode*, int> > nodes_levels;

        int levelmax = 0;
        int level = 0;
        TreeNode *node;

        nodes_levels.push_back(make_tuple(root, level));

        while (!nodes_levels.empty()){
            tie(node, level) = nodes_levels.back();
            nodes_levels.pop_back();
            while (node){
                if (node->left){
                    nodes_levels.push_back(make_tuple(node->left, level+1));
                }
                if (level == levelmax){
                    output.push_back(node->val);
                    levelmax += 1;
                }
                level += 1;
                node = node->right;
            }
        }
        return output;
    }
};
