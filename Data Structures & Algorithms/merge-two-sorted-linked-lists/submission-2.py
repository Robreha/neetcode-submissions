# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2: #While they aren't at the end of the list
            if list1.val <= list2.val: #Basically checks if which list is smaller, prefrence for l1 if = 
                node.next = list1 #Empty Node points to smaller node of the 2
                list1 = list1.next #iterate l1
            else: #l1> l2
                node.next = list2 
                list2 = list2.next

            node = node.next #Keeps iterating

        #Wht if one of the list ends 
        node.next = list1 or list2

        #Node did all the work of reorganizing now go back to dummy and return the new list
        return dummy.next 












