# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        prev = None
        stack = []
        sol = []
        # reverse the linked list
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        
        while head != None:

            while len(stack) != 0 and stack[-1] <= head.val:
                stack.pop()

            if len(stack) == 0:
                sol.append(0)
            else:
                sol.append(stack[-1])

            stack.append(head.val)
            head = head.next

        sol.reverse()
        
        return sol
