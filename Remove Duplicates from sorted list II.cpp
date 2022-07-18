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
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL || head->next == NULL)
            return head;
        ListNode *temp = head;
        ListNode *temp1 = head;
        ListNode *temp2 = head->next;
        while(temp2 != NULL)
        {
            if(temp->val == temp2->val)
            {
                if(temp == head)
                {
                    while(temp-> val == temp2->val)
                    {
                        temp->next = temp2->next;
                        delete temp2;
                        temp2 = temp->next;
                        if(temp2 == NULL)
                        {
                            delete temp;
                            return temp2;
                        }
                            
                    }
                    delete temp;
                    head = temp2;
                    temp = temp2;
                    temp2 = temp2->next;
                }
                else
                {
                    while(temp-> val == temp2->val)
                    {
                        temp->next = temp2->next;
                        delete temp2;
                        temp2 = temp->next;
                        if(temp2 == NULL)
                            break;
                            
                    }
                    temp1->next = temp2;
                    delete temp;
                    temp = temp1;
                }
                
            }
            else
            {
                temp1 = temp;
                temp = temp->next;
                temp2 = temp2->next;
            }
        }
        return head;
    }
};
