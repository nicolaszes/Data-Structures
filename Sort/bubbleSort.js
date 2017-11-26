function bubbleSort (array) {
  if (array.length < 2) {
    return array;
  }

  for (let i = 0; i < array.length; i++) {
    // 代码优化，加上 i => array.length - i - 1
    for (let j = 0; j < array.length - i - 1; j++) {
      if (array[j] > array[j + 1]) {
        // 解构交换数组元素的位置
        [array[j], array[j + 1]] = [array[j + 1], array[j]];
      }
    }
  }

  return array;
}

// 交换数组项的值
function swap (a, b) {
  let aux = a;
  a = b;
  b = aux;
}

console.log(bubbleSort([4, 2, 5, 1, 6]))
