# Problem: Reverse Linked List
# Reverse the order of nodes in a singly linked list.

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    rev = reverse_list(head)
    print('Sample Input:')
    print('1 -> 2 -> 3 -> 4')
    print('\nSample Output:')
    while rev:
        print(rev.val, end=' ')
        rev = rev.next

# Time: O(n)
# Space: O(1)