/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addVal(l1, l2, 0);
    }

private:
    ListNode* addVal(ListNode* l1, ListNode* l2, int incr) {
        if ((l1 == NULL) && (l2 == NULL))
        {
            if (incr != 0)
            {
                return new ListNode(incr);
            }

            return NULL;
        }

        int val1 = 0;
        int val2 = 0;
        ListNode* next1 = NULL;
        ListNode* next2 = NULL;
        if (l1 != NULL)
        {
            next1 = l1->next;
            val1 = l1->val;
        }

        if (l2 != NULL)
        {
            next2 = l2->next;
            val2 = l2->val;
        }

        ListNode* l3 = new ListNode(0);
        int result = val1 + val2 + incr;
        if (result >= 10)
        {
            incr = 1;
            l3->val = result - 10;
        }
        else
        {
            incr = 0;
            l3->val = result;
        }

        l3->next = addVal(next1, next2, incr);
        return l3;
    }
};

void printListNode(ListNode* l1)
{
    if (l1 != NUll)
    {
        if (l1->next != NULL)
        {
            cout<<l1->val<<"->";
        }
        else
        {
            cout<<l1->val<<endl;
        }
    }


}

int main()
{
    ListNode* l1 = new ListNode(2);
    ListNode* l1_2 = new ListNode(4);
    ListNode* l1_3 = new ListNode(3);
    l1->next = l1_2;
    l1_2->next = l1_3;
    printListNode(l1);
    ListNode* l2 = new ListNode(5);
    ListNode* l2_2 = new ListNode(6);
    ListNode* l2_3 = new ListNode(4);
    l2->next = l2_2;
    l2_2->next = l2_3;
    print(l2);
    ListNode* l3 = Solution().addTwoNumbers(l1, l2);
    print(l3);
}