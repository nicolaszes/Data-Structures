var isPalindrome = function (head) {
  let slow = head
  let fast = head

  if (head == null || head.next == null) {
    return true
  }

  while (fast && fast.next) {
    slow = slow.next
    fast = fast.next.next
  }

  let p1 = head
  let p2 = null
  if (fast != null) {
    p1 = p1.next
  }
  // 链表反转
  while (p1) {
    [p1.next, p2, p1] = [p2, p1, p1.next]
  }

  while (p2) {
    if (p2.val != head.val) return false
    p2 = p2.next
    head = head.next
  }

  return true
};