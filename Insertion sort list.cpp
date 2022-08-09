/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        
        ListNode *temp1 = head->next;
        ListNode *temp2 = head;
        ListNode *temp3 = NULL;
        ListNode *temp4 = NULL;
        
        while(temp1 != NULL)
        {
                temp3 = head;
            temp4 = head;
                while(temp3 != NULL)
                {
                    if(temp3 == temp1)
                        break;
                    if(temp3->val >= temp1->val)
                    {
                        if(temp3 == head)
                        {
                            temp2->next = temp1->next;
                            temp1->next = temp3;
                            head = temp1;
                            temp1 = temp2;
                        }
                        else
                        {
                            temp2->next = temp1->next;
                            temp4->next = temp1;
                            temp1->next = temp3;
                            temp1 = temp2;
                        }
                        break;
                    }
                    
                    temp4 = temp3;
                    temp3 = temp3->next;
                }
            temp2 = temp1;
            temp1 = temp1->next;
                
        }
        return head;
    }
};
