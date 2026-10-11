# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        point = head
        while point:
            length += 1
            point = point.next

        dummy = ListNode(0, head)
        go = dummy
        for i in range(length - n): #Stops right before, [1,2,3,] n=1 --> [1]
            go = go.next 
        
        go.next = go.next.next #Skips that node [1] -->[1,3]
        

        return dummy.next 
