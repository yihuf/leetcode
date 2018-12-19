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
    def __addVal__(self, l1, l2, incr):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type incr: int
        :rtype: ListNode
        """
        val1 = 0
        val2 = 0
        next1 = None
        next2 = None

        if l1 == None and l2 == None:
            if incr != 0:
                return ListNode(incr)
            else:
                return None

        if l1 != None:
            val1 = l1.val
            next1 = l1.next
        if l2 != None:
            val2 = l2.val
            next2 = l2.next

        l3 = ListNode(0)
        result = val1 + val2 + incr
        if(result >= 10):
            l3.val = result - 10
            incr = 1
        else:
            l3.val = result
            incr = 0

        l3.next = self.__addVal__(next1, next2, incr)
        return l3        


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return self.__addVal__(l1, l2, 0)

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

l3 = Solution().addTwoNumbers(l1, l2)
printListNode(l3)