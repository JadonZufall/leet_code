"""
This is a somewhat better solution I came up with it's a bit messier though.
Runtime 67ms, Beats 95.91%
Memory 13.9mb, Beats 85.99%
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    first_node = ListNode(val=0, next=None)
    this_node = first_node
    target_1, target_2 = l1, l2
    carry_val = False
    while True:
        # Loop over each number in the nodes
        val_1, val_2, val_3 = 0, 0, 0

        # There is still some value to be added
        if target_1:
            val_1 = target_1.val
        if target_2:
            val_2 = target_2.val
        if carry_val:
            # If carry value then carry the value of 1
            val_3 = 1

        # Calculate the sum
        this_val = val_1 + val_2 + val_3

        # Check if number is required to carry
        if this_val > 9:
            this_val = this_val - 10
            carry_val = True
        else:
            carry_val = False

        # Set the value of this node
        this_node.val = this_val

        # Move the targets to next node
        if target_1:
            target_1 = target_1.next
        if target_2:
            target_2 = target_2.next

        if not target_1 and not target_2 and not carry_val:
            # No more nodes are left
            break

        # Create next node
        this_node.next = ListNode()

        # Move to the next node for next itteration
        this_node = this_node.next
    return first_node
