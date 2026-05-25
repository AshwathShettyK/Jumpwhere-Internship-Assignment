# Problem: Remove Nth Node From End
# Remove the nth node from the end of a linked list.

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = remove_nth_from_end(head, 2)
    print('Sample Input:')
    print('1 -> 2 -> 3 -> 4 -> 5, n = 2')
    print('\nSample Output:')
    while res:
        print(res.val, end=' ')
        res = res.next

# Time: O(n)
# Space: O(1)