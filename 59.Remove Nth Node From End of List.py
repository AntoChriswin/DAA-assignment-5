class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy

    # Move the second pointer n steps forward
    for _ in range(n + 1):
        second = second.next

    # Move both pointers together until second reaches the end
    while second is not None:
        first = first.next
        second = second.next

    # Remove the nth node
    first.next = first.next.next

    return dummy.next


# Example usage
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

new_head1 = removeNthFromEnd(head1, 2)
while new_head1:
    print(new_head1.val, end=" ")
    new_head1 = new_head1.next
# Output: 1 2 3 5

print()

head2 = ListNode(1)
new_head2 = removeNthFromEnd(head2, 1)
while new_head2:
    print(new_head2.val, end=" ")
    new_head2 = new_head2.next
# Output: (empty list)

print()

head3 = ListNode(1)
head3.next = ListNode(2)
new_head3 = removeNthFromEnd(head3, 1)
while new_head3:
    print(new_head3.val, end=" ")
    new_head3 = new_head3.next
# Output: 1
