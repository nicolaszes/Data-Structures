/**
 * @param {string} s
 * @return {boolean}
 * Time: O(n)
 * Space: O(n)
 */
var isValid = function(s) {
  let stack = []
  let paren_map = {
      ')': '(',
      ']': '[',
      '}': '{'
  }
  
  for (let c of s) {
      if (!paren_map[c]) {
          stack.push(c)
      } else if (stack.length === 0 || paren_map[c] != stack.pop()) {
          return false
      }
  }
  
  return stack.length === 0
};


/**
 * @param {string} s
 * @return {boolean}
 * Time: O(n^2)
 * Space: O(n^2)
 */
var isValid = function(s) {
    let length = 0
    do {
        length = s.length
        // replace 本身是 O(n)的时间复杂度
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    } while (length !== s.length)
    return s.length === 0
};