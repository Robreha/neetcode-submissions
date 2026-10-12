# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) #dummy node to help you track pointers

        l = dummy #left pointer -->None
        r = head #right pointer -->head

        for i in range(n): #Right pointer iterates until index before n --> [0,n)
            r = r.next
        
        while r:  #Now slide both pointers until you reach end of the list
            r = r.next
            l = l.next #Left pointer should end at index before Nth term

        l.next = l.next.next #Skip that node you're trying to remove

        return dummy.next #Returns list -(None, tail] = [head, tail]