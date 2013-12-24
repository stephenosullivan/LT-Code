#include<iostream>
using namespace std;


//Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
       if(!head)
      return false;
   
    ListNode *first=head,*second=head;
   
  
    while(first->next!=NULL && first->next->next!=NULL){
          	first=first->next->next;
	second=second->next;
	if(first == second){
	  return true;
	}

      }
    //  it=it->next;
    
    return false;
    }
};


int main(){
  ListNode a(1);
  ListNode b(2);
  a.next=&b;
  //cout << a.val << " " << b.val << endl; 
  //cout << a.next->val << endl;


  Solution1 test;
  cout << test.hasCycle(&a) << endl;
}
