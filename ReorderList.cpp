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
    void reorderList(ListNode* head) {
       ListNode *temp = head;
        vector<ListNode*>v;
        while(temp != NULL)
        {
            v.push_back(temp);
            temp = temp -> next;
        }
        
        int n = v.size();
        int a = n-1;
        int i = 0;
        
        while(i < a)
        {
            v[i]->next = v[a];
            v[a]->next = v[++i];
            a--;
            if(i == n/2)
            {
                v[i]->next = NULL;
                break;
            }
            if(a == n/2)
            {
                v[a]->next = NULL;
                break;
            }
            
                
        }
    }
};
