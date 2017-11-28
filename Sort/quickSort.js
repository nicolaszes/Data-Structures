function quickSort (arr, left, right) {
  if (arr.length < 2) {
    return arr;
  }

  let index = partition(arr, left, right)
  console.log(index)

  if (left < index - 1) {
    quickSort(arr, left, index -1)
  }

  if (index < right) {
    quickSort(arr, index, right)
  }
}

function partition (arr, left, right) {
  let pivot = arr[Math.floor((right + left) / 2)];
  let i = left;
  let j = right;

  while (i <= j) {
    while (arr[i] < pivot) {
      i++;
    }

    while (arr[j] > pivot) {
      j--;
    }

    if (i <= j) {
      [arr[i], arr[j]] = [arr[j], arr[i]]
      i++;
      j--;
    }
  }

  return i
}

let arr = [1, 3, 6, 4, 2, 5];
quickSort(arr, 0, arr.length - 1)
console.log(arr)
