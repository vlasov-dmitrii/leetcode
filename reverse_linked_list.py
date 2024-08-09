

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head):
    previous_node = None
    node = head
    while node:
        previous_next = node.next
        node.next = previous_node
        previous_node = node
        node = previous_next
    return previous_node

