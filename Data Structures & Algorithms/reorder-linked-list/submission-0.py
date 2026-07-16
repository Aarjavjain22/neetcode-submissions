# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step 1 find mid
        #reverse second haalf
        #combine both
        if not head:
            return
        slow=head
        fast=head

        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next

        
        cur=slow.next
        slow.next=None
        prev=None

        while cur:
            temp=cur.next
            cur.next= prev
            prev=cur
            cur=temp

        list1= head
        list2= prev

        output=ListNode()
        cur=output

        while list1 and list2:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
            
            cur.next = list2
            cur = cur.next
            list2 = list2.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
