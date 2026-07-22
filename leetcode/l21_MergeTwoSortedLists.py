"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

#solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2: #bucle while both lists have nodes
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
        
        """
        this problem is solved by using a dummy node to simplify the merging process. 
        We iterate through both lists, comparing their values and appending the smaller 
        value to the merged list. Once we reach the end of one list, we append the remaining 
        nodes of the other list to the merged list. Finally, 
        we return the next node of the dummy, which is the head of the merged sorted list. 
        """