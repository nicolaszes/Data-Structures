function fact (x, y = 1) {
  if (x === 1) {
    return x * y;
  } else {
    let res = x * y;
    return fact(x - 1, res);
  }
}

console.log(fact(6))
console.log([2, 4, 6].reduce((pre, next, index, arr) => pre + next))
