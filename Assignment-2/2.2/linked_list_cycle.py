# Problem: Linked List Cycle
# Detect whether a linked list contains a cycle.

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3)))
    head.next.next.next = head.next
    print('Sample Input:')
    print('1 -> 2 -> 3 -> 2')
    print('\nSample Output:')
    print(has_cycle(head))

# Time: O(n)
# Space: O(1)