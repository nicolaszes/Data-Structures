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
    if (sum >= coins[i]) {
      let n = Math.round(sum / coins[i])
      if (n >= coinsNum[i]) {
        n = coinsNum[i]
      }
      sum -= Math.round(n * coins[i])
      console.log(`用了${n}个${coins[i]}元硬币`)
    }
  }
}
main()