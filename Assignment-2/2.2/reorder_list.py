# Problem: Reorder List
# Reorder list as L0 -> Ln -> L1 -> Ln-1 -> ...

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def reorder_list(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    first = head
    second = prev
    while second.next:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder_list(head)
    print('Sample Input:')
    print('1 -> 2 -> 3 -> 4')
    print('\nSample Output:')
    while head:
        print(head.val, end=' ')
        head = head.next

# Time: O(n)
# Space: O(1)