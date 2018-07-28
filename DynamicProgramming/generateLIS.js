function dpIndex (arr) {
  // 创建长度为 arr.length 的数组，其中每一项都是 0
  let dp = Array.from(new Array(arr.length)).map(item => 0)

  for (let i = 0; i < arr.length; i++) {
    dp[i] = 1

    for (let j = 0; j < i; j++) {
      if (arr[i] > arr[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1)
      }
    }
  }

  return dp
}

function generateLIS(arr, dp) {
  let dp_max = Math.max(...dp)
  let index = dp.findIndex(e => e === dp_max)
  let result = Array.from(new Array(dp_max)).map(item => 0)
  result[--dp_max] = arr[index]

  for (let i = index; i >= 0; i--) {
    if (arr[i] < arr[index] && dp[i] === dp[index] - 1) {
      result[--dp_max] = arr[i]
      index = i
    }
  }

  return result
}

var arr = [1, 2, 4, 3, 5, 4, 6, 8, 9, 7]

console.log(generateLIS(arr, dpIndex(arr)))