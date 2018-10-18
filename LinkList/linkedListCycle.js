/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
  let [ fast, slow ] = [ head, head ]
  while(slow && fast && fast.next) {
    slow = slow.next
    fast = fast.next.next
    
    if (Object.is(slow, fast)) {
      return true
    }
  }
  return false
};