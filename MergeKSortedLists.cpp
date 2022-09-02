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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        vector<int> v;
        for(int i = 0 ; i<n ; i++)
        {
            ListNode *temp = lists[i];
            while(temp != NULL)
            {
                v.push_back(temp->val);
                temp = temp->next;
            }
        }
        
        sort(v.begin(),v.end());
        ListNode *head = NULL;
        ListNode *temp1 = NULL;
        n = v.size();
        
        for(int i = 0 ; i<n ; i++)
        {
            if(head == NULL)
            {
                ListNode * temp = new ListNode;
                temp ->val = v[i];
                temp ->next = NULL;
                head = temp;
                temp1 = temp;
            }
            else
            {
                ListNode *temp = new ListNode;
                temp ->val = v[i];
                temp ->next = NULL;
                temp1 ->next = temp;
                temp1 = temp;
            }
        }
        
        return head;
            
    }
};
