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
    int pairSum(ListNode* head) {
        int max=0;
        vector<int> sum;
        int counter = 0;
        
        while(head != NULL)
        {
            sum.push_back(head->val);
            head = head ->next;
            counter++;
        }
        
        for(int i = 0 ; i < counter/2 ; i++)
        {
            if(sum[i] + sum[counter - i - 1] > max)
                max = sum[i] + sum[counter - i - 1];
        }
        
        return max;
    }
};
