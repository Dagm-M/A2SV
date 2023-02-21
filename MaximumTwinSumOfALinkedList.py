# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        maxSum = []

        fast = head
        slow = head

        while fast != None:
            fast = fast.next.next
            maxSum.append(slow.val)
            slow = slow.next

        for i in range(len(maxSum)-1 , -1 , -1):
            maxSum[i] += slow.val
            slow = slow.next


        return max(maxSum)
