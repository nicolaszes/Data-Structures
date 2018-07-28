/**
 * 最大子数组之和
 * @param arr 
 */
function maxArr (arr) {
  let s_sum = 0
  let s_max = 0

  for (let i in arr) {
    s_sum += arr[i]
    if (s_sum >= s_max) {
      s_max = s_sum
    } else if (s_sum < 0) {
      s_sum = 0
    }
  }
  return s_max
}