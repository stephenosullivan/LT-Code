/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
  //Reverse a linked list between nodes m and n
    ListNode *reverseBetween(ListNode *head, int m, int n) {
      //Edge case: zero length
        if(m==n){
            return head;
        }

	//declarations
        ListNode *pm, *pn, *p1, *p2 ,*px;
        int cntm = m-1;
        int cntn = n-1;
        int cntmn;
        pm = head;
        pn = head;
        
	//place a pointer at n
        while(cntn>0){
            pn = pn->next;
            --cntn;
        }
        
	//place a pointer px right before m
        if(cntm==0){
            px = pn;
        }
        else{
            px = head;
            while(cntm>0){
                if(cntm!=1){
                    px = px->next;
                }
                pm = pm->next;
                --cntm;
            }
            px->next = pn;
        }
        
	//place pointer just after n
        p2 = pn->next;
        
	//iterate over the elements to be reversed
        for(int i = n-m; i>0; --i){
            cntmn = i;
            p1 = pm;
        
            while(cntmn>1){
                p1 = p1->next;
                --cntmn;
            }
        
            pn->next = p1;
            pn = p1;
        }

	//link the end of the chain
        pm->next = p2;
        
	//edge case: first element contained in reversed list
        if(pm == head)
            return px;
            
        return head;
    }
};
