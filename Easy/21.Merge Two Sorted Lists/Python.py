# find which value is smaller
# put smaller value first
# repeat


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        ReturnList = ListNode()
        tail = ReturnList
        
        if not temp1:
            return temp2
        if not temp2:
            return temp1
        
        while temp1 and temp2: # while both is not empty
            if(temp1.val <= temp2.val):
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next
            tail = tail.next
            
            # append any remaining nodes
            if temp1:
                tail.next = temp1
            if temp2:
                tail.next = temp2
        
        return ReturnList.next
                

# Helper function: convert Python list to linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Helper function: print linked list
def print_linkedlist(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))

# Main function for testing
def main():
    # Example lists
    list1 = list_to_linkedlist([1])
    list2 = list_to_linkedlist([4])

    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)

    print("Merged list:")
    print_linkedlist(merged)

if __name__ == "__main__":
    main()
