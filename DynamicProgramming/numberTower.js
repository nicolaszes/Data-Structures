let arr = [9, 12, 15, 10, 6, 8, 2, 18, 9, 5, 19, 7, 10, 4, 16, 7, 8, 9, 20, 11, 12]
function m (a, b) {
  if (a === 5) return arr[b]
  console.log(a + 1, a + b + 1)
  console.log(a + 1, a + b + 2)

  let L = m(a + 1, a + b + 1)
  let R = m(a + 1, a + b + 2)

  if ( L > R) {
    return L + arr[b]
  }
  return R + arr[b]
}

m(0, 0)