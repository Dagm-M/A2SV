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
class Solution
{
public:
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        ListNode *merged = NULL;
        ListNode *l1 = list1;
        ListNode *l2 = list2;
        ListNode *temp = l2;
        if (list1 && list2 == NULL)
            return list1;
        else if (list1 == NULL)
            return list2;
        else if (list2 == NULL)
            return list1;
        if (list1->val > list2->val)
            merged = list2;
        else
            merged = list1;

        while (l1 && l2 != NULL)
        {
        
            if (l1->val > l2->val)
            {
                if (l2->next != NULL)
                {
                    if (l2->next->val < l1->val)
                        l2 = l2->next;
                    else
                    {
                        temp = l2->next;
                        l2->next = l1;
                        l2 = temp;
                    }
                }
                else
                {
                    if(l2->val < l1->val)
                    {
                        l2->next = l1;
                        l2 = NULL;
                    }
                    else
                    {
                        temp = l1->next;
                        l1->next = l2;
                        l2->next = temp;
                        l2 = NULL;
                    }
                }
            }
            else
            {
                if (l1->next != NULL)
                {
                    if (l1->next->val <= l2->val)
                        l1 = l1->next;
                    else
                    {
                        temp = l1->next;
                        l1->next = l2;
                        l1 = temp;
                    }
                }
                else
                {
                    if(l1->val < l2->val)
                    {
                        l1->next = l2;
                        l1 = NULL;
                    }
                    else
                    {
                        if(temp != l2)
                        {
                            temp = l2->next;
                            l2->next = l1;
                            l1->next = temp;
                            l1 = NULL;
                        }
                        else
                        {
                            l1->next = l2;
                            l1 = NULL;
                        }
                    }
                }
            }
        }
        return merged;
    }
};
