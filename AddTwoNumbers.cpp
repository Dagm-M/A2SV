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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
       vector<int> num;
        ListNode *l3 = new ListNode;
        l3->val = -1;
        ListNode *begin = NULL;
        while(l1 != NULL || l2 !=NULL)
        {
            if(l1 == NULL)
            {
                num.push_back(l2->val);
                l2 = l2->next;
            }
            else if(l2 == NULL)
            {
                num.push_back(l1->val);
                l1 = l1->next;
            }
            else
            {
                num.push_back(l1->val + l2->val);
                l1 = l1->next;
                l2 = l2->next;
            }
            
            
        }
        int n = num.size();
        for(int i = 0; i<n ; i++)
        {
            if(num[i] >= 10)
            {
                num[i] = num[i] % 10;
                if(i == n-1)
                {
                    num.push_back(1);
                    n = num.size();
                }
                else
                    num[i+1] += 1;
            }
            
                if(l3->val == -1)
                {
                    ListNode *temp = new ListNode;
                    temp->val = num[i];
                    temp->next = NULL;
                    l3 = temp;
                    begin = temp;
                }
                else
                {
                    ListNode *temp = new ListNode;
                    temp->val = num[i];
                    temp->next = NULL;
                    l3->next = temp;
                    l3 = temp;
                }
        }
        return begin;
    }
};
