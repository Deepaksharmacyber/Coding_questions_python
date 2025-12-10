# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes duplicates from a sorted linked list.
        
        Approach:
        - Iterate through the list
        - If current node's value equals next node's value, skip the next node
        - Otherwise, move to the next node
        
        Time Complexity: O(n) where n is the number of nodes in the linked list
        Space Complexity: O(1) as we only use a constant amount of extra space
        
        Args:
            head: Head node of the sorted linked list
            
        Returns:
            Head node of the linked list with duplicates removed
        """
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Skip the duplicate node
                curr.next = curr.next.next
            else:
                # Move to the next node
                curr = curr.next
        
        return head