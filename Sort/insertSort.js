function insertSort (arr) {
  if (arr.length < 2) {
    return arr;
  }

  for (let i = 1; i < arr.length; i++) {
    while (i >= 1 && arr[i - 1] > arr[i]) {
      [arr[i], arr[i - 1]] = [arr[i - 1], arr[i]]
      i--
    }
  }
  return arr
}

console.log(insertSort([3, 2, 5, 4, 6, 1]))
