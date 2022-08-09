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
    ListNode* middleNode(ListNode* head) {
        vector<ListNode*> links;
        int counter = 0;
        while(head != NULL)
        {
            links.push_back(head);
            head = head->next;
            counter++;
        }
        counter = (counter/2 );
        return links[counter];
    }
};
