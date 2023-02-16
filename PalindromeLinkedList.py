# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isListPalindrome(self, leftNode, rightNode):
        if rightNode == None:
            return [True,leftNode]

        resultSublist = self.isListPalindrome(leftNode, rightNode.next)
        res = resultSublist[0]
        leftNode = resultSublist[1]

        if not res:
            return [False,None]

        if leftNode.val == rightNode.val:
            result = True
        else:
            result = False

        leftNode = leftNode.next

        return [result,leftNode]

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        leftNode = head
        rightNode = head.next

        return self.isListPalindrome(leftNode,rightNode)[0]
