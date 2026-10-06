# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1.Compare lists node by node
        """
        h1 = list1
        h2 = list2
        temp = ListNode()
        temp2 = temp

        while (h1 and h2):
            if (h1.val < h2.val):
                temp2.next = h1
                h1 = h1.next
            else:
                temp2.next = h2
                h2 = h2.next
                
            temp2 = temp2.next 

        temp2.next = h1 or h2
        return temp.next




                    
                    

                    
            
        