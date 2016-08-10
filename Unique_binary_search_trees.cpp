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
    vector<TreeNode*> generateTrees(int n) {
        if (n==0){
            vector<TreeNode*> ret;
            return ret;
        }
        dp = vector<vector<vector<TreeNode*>>>(n+1, vector<vector<TreeNode*>>(n+1, vector<TreeNode*>(1,NULL)));
        return recursiveGenerate(0,n);
    }

    vector<TreeNode*> recursiveGenerate(int i, int j){
        if (dp[i][j][0] == NULL && i!=j){
            dp[i][j].pop_back();
            for (int k = i; k < j; ++k){
                for (TreeNode* leftNode: recursiveGenerate(i, k)){
                    for (TreeNode* rightNode: recursiveGenerate(k+1,j)){
                        TreeNode *head = new TreeNode(k+1);
                        head->left = leftNode;
                        head->right = rightNode;
                        dp[i][j].push_back(head);
                    }
                }
            }
        }
        return dp[i][j];
    }

    vector<vector<vector<TreeNode*> > > dp;