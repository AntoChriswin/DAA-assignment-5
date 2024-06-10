class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    # Initialize a dummy head for the result linked list
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Traverse both linked lists
    while l1 or l2 or carry:
        # Get the current values or 0 if one list is shorter
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and the new carry
        total = val1 + val2 + carry
        carry = total // 10
        new_val = total % 10

        # Create a new node for the result
        current.next = ListNode(new_val)
        current = current.next

        # Move to the next nodes in l1 and l2
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Return the result list starting from the next node after dummy head
    return dummy_head.next

# Helper function to create linked list from list of numbers
def create_linked_list(nums):
    dummy_head = ListNode(0)
    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next

# Helper function to print linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# Example usage
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = add_two_numbers(l1, l2)
print_linked_list(result)  # Output: [7, 0, 8]

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = add_two_numbers(l1, l2)
print_linked_list(result)  # Output: [0]

l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])
result = add_two_numbers(l1, l2)
print_linked_list(result)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
