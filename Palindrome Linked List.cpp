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
    bool isListPalindrome(ListNode* &leftNode, ListNode* &rightNode)
    {
        bool result;
        if(rightNode == NULL)
          return true;
       
        bool resultSublist = isListPalindrome(leftNode, rightNode->next);
        
        if(!resultSublist) 
            return false;

        if(leftNode->val == rightNode->val)
            result = true; 
        else
            result = false;
        
        leftNode = leftNode->next;
        return result;
    }
    
    bool isPalindrome(ListNode* head) {
        ListNode *leftNode = head;
        ListNode *rightNode = head->next;
        return isListPalindrome(leftNode,rightNode);
    }
};
