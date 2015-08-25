//
//  construct-binary-tree-form-inorder-and-postorder-traversal.cpp
//
//
//  Created by Stephen O'Sullivan on 8/23/15.
//
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (!postorder.empty()){
            vector<int>::iterator iter;
            vector<int>::reverse_iterator rev_iter;

            // Save computations by checking for series of left or right branches
            bool reverseCheck  = true;
            for(iter=inorder.begin(), rev_iter=postorder.rbegin(); iter!=inorder.end(), rev_iter!=postorder.rend(); ++iter, ++rev_iter){
                if(*iter!=*rev_iter){
                    reverseCheck=false;
                    break;
                }
            }

            if (inorder==postorder){
                TreeNode* node = new TreeNode(postorder.back());
                TreeNode* head = node;
                for(rev_iter=inorder.rbegin()+1;rev_iter!=inorder.rend();++rev_iter){
                    node->left = new TreeNode(*rev_iter);
                    node = node->left;
                }
                return head;
            }


            else if (reverseCheck){
                TreeNode* node = new TreeNode(postorder.back());
                TreeNode* head = node;
                for(rev_iter=postorder.rbegin()+1;rev_iter!=postorder.rend();++rev_iter){
                    node->right = new TreeNode(*rev_iter);
                    node = node->right;
                }
                return head;
            }

            // Need to partition
            TreeNode* node = new TreeNode(postorder.back());
            if (inorder.size() > 1){
                int index = find(inorder.begin(), inorder.end(), postorder.back()) - inorder.begin();
                postorder.pop_back();
                vector<int> inorderRightSub(inorder.begin()+index+1, inorder.end());
                vector<int> postorderRightSub(postorder.begin()+index, postorder.end());
                vector<int> inorderLeftSub(inorder.begin(), inorder.begin()+index);
                vector<int> postorderLeftSub(postorder.begin(), postorder.begin()+index);

                node->right = buildTree(inorderRightSub, postorderRightSub);
                node->left = buildTree(inorderLeftSub, postorderLeftSub);
            }
            return node;
        }
        else{
            return NULL;
        }

    }
};



void printNode(TreeNode* node){
    while (node != NULL) {
        printNode(node->left);
        cout << node->val << endl;;
        printNode(node->right);
        break;

    }
}

int main(){
    vector<int> inorder = {1,3,2};
    vector<int> postorder = {3,2,1};

    Solution sol;
    TreeNode* node = sol.buildTree(inorder, postorder);
    cout << node->val << endl;
    cout << node->right->val << endl;
    cout << node->right->left->val << endl;

    printNode(node);


}