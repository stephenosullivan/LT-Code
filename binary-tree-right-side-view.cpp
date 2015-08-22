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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> output;

        vector<TreeNode*> nodes_to_visit;
        nodes_to_visit.push_back(root);
        vector<int> node_levels;
        node_levels.push_back(1);

        int levelmax = 0;
        int level = 1;
        TreeNode *node;

        while (!nodes_to_visit.empty()){
            node = nodes_to_visit.back();
            nodes_to_visit.pop_back();
            level = node_levels.back();
            node_levels.pop_back();
            while (node){
                //cout << node->val << endl;
                if (node->left){
                    nodes_to_visit.push_back(node->left);
                    node_levels.push_back(level+1);
                }
                //cout << "level " << level << " " << levelmax << endl;
                if (level > levelmax){

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