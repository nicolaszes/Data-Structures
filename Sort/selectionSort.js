function selectionSort (arr) {
  if (arr.length < 2) {
    return arr;
  }

  // 找出数组中最小值，将其放到第一位
  // 找出数组第二小的值，将其放到第二位
  for (let i = 0; i < arr.length; i++) {
    let smallest = arr[i];
    let location = i;

    for (let j = i; j < arr.length; j++) {
      if (arr[j] < smallest) {
        smallest = arr[j];
        location = j;
      }
    }

    if (i !== location) {
      [arr[i], arr[location]] = [arr[location], arr[i]]
    }
  }

  return arr;
}

console.log(selectionSort([2, 4, 6, 5, 1, 3]))
