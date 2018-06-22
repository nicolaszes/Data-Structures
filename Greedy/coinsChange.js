function main(sum) {
  const coins = [1, 2, 5, 10, 20, 50, 100]
  let coinsNum = [10, 10, 10, 10, 10, 10, 10]

  let total = 0
  for (let i in coins) {
    total += total + coins[i] * coinsNum[i]
  }
  console.log(total)

  // 当输入的金额比收银员的总金额多，无法进行找零
  if (sum > total) {
    console.log('数据有错')
    return null
  }

  for (let i = coins.length - 1; i >= 0; i--) {
    // 当 sum小于当前的硬币的面值，跳过此步骤，进入下一个循环
    if (sum < coins[i]) {
      continue
    }

    // 向下取整获得当前需要找零的硬币个数
    let n = Math.floor(sum / coins[i])
    // 如果 n 大于当前硬币的总数，重置 n = 当前硬币的总数
    if (n >= coinsNum[i]) {
      n = coinsNum[i]
    }
    sum -= Math.round(n * coins[i])
    console.log(`用了${n}个${coins[i]}元硬币`)
  }
}
main(256)