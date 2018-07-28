let w = [2, 1, 3, 2, 2]
let v = [12, 10, 20, 15, 18]

function knapsack (i, j) {
  if (i === -1 || j === 0) return 0

  if (j >= w[i]) {
    let m1 = knapsack(i - 1, j)
    let m2 = knapsack(i - 1, j - w[i]) + v[i]

    if (m1 > m2) {
      return m1
    }
    return m2
  }

  return knapsack(i - 1, j)
}

knapsack(3, 8)