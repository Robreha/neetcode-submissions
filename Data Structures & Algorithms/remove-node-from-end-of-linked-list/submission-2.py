# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        point = head
        length = 0 
        while point:
            length +=1 
            point = point.next
        
        curr = dummy
        for i in range(0 ,length - n):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next
