#include <iostream>
using namesapce std;

//Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
  //Detect the position of a cycle if it exists
  ListNode *detectCycle(ListNode *head) {
    ListNode *fast, *slow;

    //Check for edge cases
    if(head==NULL)
      return NULL;
    slow = head;
    if(slow->next == NULL){
      return NULL;
    } 
    else slow = slow->next;

    fast = head->next->next;    

    //Find the position where the "fast" pointer equals the "slow" one
    while(fast!=slow){
      if(slow->next == NULL){
	return NULL;
      }
      else slow = slow->next;

      if(fast->next == NULL || fast->next->next == NULL){
	return NULL;
      }
      else fast = fast->next->next;
    }

    //Add the length of one cycle to the head and slow pointer to find the cycle location
    while(head!=slow){
      head = head-> next;
      slow = slow->next;
    }
	
    return slow;
  }
};

