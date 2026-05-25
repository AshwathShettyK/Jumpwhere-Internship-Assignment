# Problem: Merge Two Sorted Lists
# Merge two sorted linked lists into one sorted list.

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def merge_two_lists(a, b):
    dummy = ListNode()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


if __name__ == '__main__':
    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    merged = merge_two_lists(a, b)
    print('Sample Input:')
    print('1 -> 2 -> 4 and 1 -> 3 -> 4')
    print('\nSample Output:')
    while merged:
        print(merged.val, end=' ')
        merged = merged.next

# Time: O(n+m)
# Space: O(1)