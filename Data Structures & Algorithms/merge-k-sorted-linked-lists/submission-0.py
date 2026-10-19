# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Merge sort -> logK
        #Loop through k lists in groups of 2 
        #Sort group, turn into one, under a while loop so keeps iterating until one big list
        #Return list 

        #Edge case list empty or null
        if not lists:
            return None

        while len(lists) > 1:
            bigList = []
            for i in range(0,len(lists),2):
                if i + 1< len(lists):
                    bigList.append(self.mergeSort(lists[i],lists[i+1]))
                else:
                    bigList.append(lists[i])
            lists = bigList
        return lists[0]



    def mergeSort(self, l1, l2):
        dummy = warrior = ListNode()

        while l1 and l2:
            if l1.val < l2.val: #deciding where warior goes
                warrior.next = l1
                l1 = l1.next 
            else:
                warrior.next = l2
                l2 = l2.next
            warrior = warrior.next #actually moving him there
        warrior.next = l1 or l2 #one of the list ends

        return dummy.next #Buddy got to sit back n watch warrior do all the work smh.


            