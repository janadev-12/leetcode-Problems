class Solution(object):
    def pairSum(self, head):
        slow = fast = head

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Calculate maximum twin sum
        maximum = 0
        first = head
        second = prev

        while second:
            total = first.val + second.val
            maximum = max(maximum, total)

            first = first.next
            second = second.next

        return maximum