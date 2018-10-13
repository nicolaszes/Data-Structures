/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
  if(head == null || head.next == null) return head;
  let prev = head;
  let cur  = head.next;

  while(prev != null && cur != null){
    // 很一般的交換
    [prev.val, cur.val] = [cur.val, prev.val]

    if(cur.next == null || cur.next.next == null) break;
    // 處理下一對node
    prev = cur.next;
    cur  = cur.next.next;     
  }   
  return head;
};