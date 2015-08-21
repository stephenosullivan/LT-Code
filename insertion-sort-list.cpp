//
//  insertion-sort-list.cpp
//
//
//  Created by Stephen O'Sullivan on 8/20/15.
//
//

#include <iostream>

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode *ptr, *FakeHeadNode;
        FakeHeadNode = new ListNode(0);
        FakeHeadNode->next = head;
        ptr = head;

        // Sweep through the list
        while (ptr && ptr->next){
            // Check if we need to sweep for the insertion pt
            if (ptr->next->val < ptr->val){
                ListNode *insert;
                insert = FakeHeadNode;

                // Find insertion pt
                while (ptr->next->val > insert->next->val){
                    insert = insert->next;
                }
                ListNode *tmp;

                // remove node
                tmp = ptr->next;
                ptr->next = ptr->next->next;

                // insert node
                tmp->next = insert->next;
                insert->next = tmp;
            }

            else{
                ptr = ptr->next;
            }
        }
        return FakeHeadNode->next;
    }
};

int main(){
    Solution sol;
    ListNode one(3);
    ListNode two(2);
    ListNode three(1);
    one.next = &two;
    two.next = &three;

