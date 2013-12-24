#include<iostream>
#include<vector>
#include<stack>
using namespace std;

// Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



class Solution_recursive{
public:
  vector<int> preorderTraversal(TreeNode *root) {
    vector<int> store;
    if(!root){
      return store;
    }
    else{
      store.push_back(root->val);
      vector<int> left = preorderTraversal(root->left);
      store.insert(store.end(),left.begin(),left.end());
      vector<int> right = preorderTraversal(root->right);
      store.insert(store.end(),right.begin(),right.end());
      return store;
    }
        
  }
};


class Solution_iterative{
public:
  vector<int> preorderTraversal(TreeNode *root) {
    vector<int> store;
    stack<TreeNode*> mystack;
    TreeNode *it, *itsave, *itsaveprevious;
    if(!root){
      return store;
    }
    it = root;
    store.push_back(it->val);
    while(true)
      {
	if(it->right){
	  mystack.push(it->right);
	}
	if(it->left){	
	  it = it->left;
	  store.push_back(it->val);
	}     
	else{
	  if(!mystack.empty()){
	    it = mystack.top();
	    mystack.pop();
	    store.push_back(it->val);
	  }
	  else{
	    break;
	  }
	}
      }
    return store;
  }
};

int main(){
  TreeNode a(1);
  TreeNode b(2);
  TreeNode c(3);
  a.left = &b;
  a.right = &c;



  Solution_iterative test;
  vector<int> test_vector = test.preorderTraversal(&a);
  for(vector<int>::iterator it = test_vector.begin();it!=test_vector.end();++it)
    cout << *it << endl;
}
