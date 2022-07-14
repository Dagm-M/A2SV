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
    ListNode* reverseList(ListNode* head) {
        ListNode *temp = head;
        ListNode *temp2 = NULL;
        ListNode *temp3 = NULL;
        
        if(temp == NULL)
            return head;
        
        if(temp->next == NULL)
            return head;
        
        if(temp->next->next == NULL)
        {
            head = temp->next;
            temp->next->next = temp;
            temp->next = NULL;
        }
        else
        {
            temp2 = temp->next;
            temp3 = temp2->next;
            while(temp3 != NULL)
            {
                if(temp == head)
                    temp->next = NULL;
                if(temp3->next == NULL)
                {
                    temp3->next = temp2;
                    temp2->next = temp;
                    head = temp3;
                    temp3 = NULL;
                }
                else
                {
                    temp2->next = temp;
                    temp = temp2;
                    temp2 = temp3;
                    temp3 = temp3->next;
                }
            }
        }

        return head;
    }
};
