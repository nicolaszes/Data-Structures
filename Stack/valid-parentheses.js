/**
 * @param {string} s
 * @return {boolean}
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