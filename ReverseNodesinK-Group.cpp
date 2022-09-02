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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k == 1)
            return head;
        vector<ListNode*> v;
        ListNode *temp = head;
        while(temp != NULL)
        {
            v.push_back(temp);
            temp = temp->next;
        }
        int a = k;
        int b = 0;
        int n = v.size();
        
        while(a <= n)
        {
            if(a == n)
                reverse(v.begin() + b, v.end());
            else
                reverse(v.begin() + b, v.begin() + a);
            b = a;
            a += k;
        }
        
        head = v[0];
        
        for(int i = 0 ; i<n ;i++)
        {
            if(i == n-1)
                v[i]->next = NULL;
            else
                v[i] ->next = v[i+1];
        }
        
        return head;
    }
};
