#include<iostream>
using namespace std;


//  Definition for binary tree with next pointer.
struct TreeLinkNode {
  int val;
  TreeLinkNode *left, *right, *next;
  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

class Solution1 {
public:
  void connect(TreeLinkNode *root) {
    if (!root){
      return;
    }
    if(!(root->left) || !(root->right))
      return;
    root->left->next = root -> right;
    if((root->left->right)){
      root->left->right=root->right->left;
    }
    connect(root->left);
    connect(root->right);
  }
};

class Solution_final{
public:
  void connect(TreeLinkNode *root) {
    if (!root){
      return;
    }
    if(!(root->left) || !(root->right))
      return;
    
    root->left->next = root->right;
    if((root->next))
      root->right->next = root->next->left; 
    connect(root->left);
    connect(root->right);
  }
};  


int main(){
  TreeLinkNode a(0);
  TreeLinkNode b(1);
  TreeLinkNode c(2);
  TreeLinkNode d(3);
  TreeLinkNode e(4);
  TreeLinkNode f(5);
  TreeLinkNode g(6);

  a.left =&b;
  a.right = &c;
  b.left = &d;
  b.right = &e;
  c.left = &d;
  c.right = &e;

  Solution_final test;
  test.connect(&a);

  //  cout << a.next.val << endl;
  cout << b.next->val << endl;
  cout << c.next << endl;
  cout << d.next->val << endl;
  cout << e.next->val << endl;

  //  cout << f.next->val << endl;
  cout << g.next << endl;

  

}
