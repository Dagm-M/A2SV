# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        left = head
        temp = None
        right = head
        position = head
        isFirst = True
        k1 = k

        while right != None:
            while right != None and k1 != 1:
                right = right.next
                k1 -= 1
                
            if right == None:
                break
                
            if temp != None:
                temp.next = right

            while left != right:
                temp = left
                left = left.next
                temp.next = right.next
                right.next = temp
            
            if isFirst:
                dummy = right
                isFirst = False

            temp = position
            position = position.next
            if position != None:  
                print(position.val)
            right = position
            left = right
            k1 = k

        return dummy
