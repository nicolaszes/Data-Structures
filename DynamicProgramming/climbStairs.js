/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // let [x, y] = [1, 1]
  // for (let i = 1; i < n; i++) {
  //     [x, y] = [y, x + y]
  // }
  // return y

  // return n <= 2 ? n : climbStairs(n - 1) + climbStairs(n - 2)

  let memMap = new Map()
  if (n <= 2) {
    return n
  } else if (memMap.has(n)) {
    return memMap.get(n)
  }
  let value = climbStairs(n - 1) + climbStairs(n - 2)
  memMap.set(n, value)
  return value
}