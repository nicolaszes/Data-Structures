function bubbleSort (arr) {
  if (arr.length < 2) {
    return arr;
  }

  for (let i = 0; i < arr.length; i++) {
    // 代码优化，加上 i => arr.length - i - 1
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // 解构交换数组元素的位置
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }

  return arr;
}


console.log(bubbleSort([4, 2, 5, 1, 6]))
