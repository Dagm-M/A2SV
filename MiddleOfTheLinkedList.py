# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # size = 0
        # temp = head

        # while temp != None:
        #     temp = temp.next
        #     size += 1

        # temp = head

        # for i in range(size//2):
        #     temp = temp.next

        # return temp

        # temp = head
        # nums = []

        # while temp != None:
        #     nums.append(temp)
        #     temp = temp.next

        # return nums[len(nums)//2]

        slow = head
        fast = head

        while fast != None:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            slow = slow.next

        return slow

     
