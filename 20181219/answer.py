# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

def printListNode(l1):
    if l1.next != None:
        print('%d->' % l1.val, end='')
        printListNode(l1.next)
    else:
        print(l1.val) 

l1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1.next = l1_2
l1_2.next = l1_3
printListNode(l1)

l2 = ListNode(5)
L2_2 = ListNode(6)
L2_3 = ListNode(4)
l2.next = L2_2
L2_2.next = L2_3
printListNode(l2)