public class Solution {


    // Definition for singly-linked list.
    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    // TODO: Implement mergeTwoLists
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        

        return null;
    }

    public static void main(String[] args) {
        ListNode list1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode list2 = new ListNode(1, new ListNode(3, new ListNode(4)));

        Solution solution = new Solution();
        System.out.println(solution.mergeTwoLists(list1, list2));
    }
}
