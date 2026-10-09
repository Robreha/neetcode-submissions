# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Slow, fast pointers to find middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Now split the lists into first and second, reverse second
        second = slow.next
        prev = slow.next = None
        #reverse list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #Now merge the lists in order of first,second, first.nxt,second.nxt, ect..
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1 , tmp2



        