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

    
    vector<int> nextLargerNodes(ListNode* head) {

        ListNode *temp = head;
        ListNode *temp2 = head->next;
        vector<int> values;
        while(temp != NULL)
        {
            temp2 = temp->next;
            while(temp2 != NULL)
            {
                if(temp2->val > temp->val)
                {
                    values.push_back(temp2->val);
                    break;
                }
                if(temp2->next == NULL)
                    values.push_back(0);
                temp2 = temp2->next;
            }
            if(temp->next == NULL)
                values.push_back(0);
            temp = temp->next;
        }
        return values;
    }
};
