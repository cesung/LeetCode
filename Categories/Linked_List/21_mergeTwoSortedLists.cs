/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution
{
    public ListNode MergeTwoLists(ListNode list1, ListNode list2)
    {
        ListNode fakeHead = new ListNode();
        ListNode curPtr = fakeHead;

        while (list1 != null && list2 != null)
        {
            if (list1.val < list2.val)
            {
                curPtr.next = list1;
                list1 = list1.next;
            }
            else
            {
                curPtr.next = list2;
                list2 = list2.next;
            }
            curPtr = curPtr.next;
        }

        if (list1 == null)
        {
            curPtr.next = list2;
        }

        if (list2 == null)
        {
            curPtr.next = list1;
        }

        return fakeHead.next;
    }
}