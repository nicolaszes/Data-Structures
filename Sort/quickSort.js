function quickSort (arr, left, right) {
  if (right - left < 2) {
    return arr;
  }

  let index = partition(arr, left, right)

  quickSort(arr, left, index - 1)
  quickSort(arr, index, right)
  return arr
}

function partition (arr, left, right) {
  // 添加随机性 Math.random，优化近似于有序的数组
  let pivot = arr[Math.floor(Math.random() * (right - left + 1) + left)];
  let i = left;
  let j = right;

  while (i <= j) {
    while (arr[i] < pivot) {
      i++;
    }

    while (arr[j] > pivot) {
      j--;
    }

    if (i > j) break

    [arr[i], arr[j]] = [arr[j], arr[i]]
    i++;
    j--;
  }

  return i
}

let arr = [6, 2, 5, 1, 8, 2, 2, 10, 2, 6, 5, 9, 2, 7, 7, 9, 7, 0, 4, 5, 10, 1, 3, 3, 2, 5, 5, 9, 0, 4, 7, 2, 8, 9, 9, 3, 6, 9, 8, 10, 2,
 0, 2, 7, 10, 2, 3, 9, 4, 6, 7, 4, 7, 2, 8, 8, 4, 0, 3, 5, 2, 2, 9, 2, 5, 1, 4, 3, 10, 4, 2, 9, 4, 10, 4, 0, 0, 2, 1, 0, 5, 10
, 9, 3, 2, 0, 8, 7, 5, 9, 5, 8, 2, 10, 3, 1, 5, 10, 4, 8, 9, 7, 10, 10, 10, 10, 7, 7, 3, 6, 4, 6, 6, 2, 4, 4, 4, 4, 2, 10, 5,
6, 9, 3, 2, 1, 0, 9, 10, 10, 2, 6, 8, 7, 0, 0, 8, 9, 4, 6, 1, 5, 0, 10, 9, 5, 0, 0, 1, 7, 10, 1, 10, 7, 8, 1, 3, 8, 10, 1, 9,
3, 10, 4, 0, 2, 4, 2, 9, 10, 0, 8, 0, 2, 10, 10, 2, 5, 5, 6, 1, 1, 9, 3, 3, 5, 6, 6, 9, 1, 1, 4, 7, 5, 9, 2, 2, 6, 7, 1]
quickSort(arr, 0, arr.length - 1)


/**
 * 三路快排
 * @param {*} arr 
 * @param {*} l 
 * @param {*} r 
 */
function quickSortIn3Ways (arr, l, r) {
  if (r - l < 2) return arr

  let ran = Math.floor(Math.random() * (r - l + 1) + l)
  swapArr(arr, l, ran)
  // [arr[l], arr[ran]] = [arr[ran], arr[l]]
  let pvoit = arr[l]

  let lt = l // arr[l+1, lt]
  let gt = r + 1 // arr[gt, r]
  let i = l + 1 // arr[lt + 1, i)

  while (i < gt) {
    if (arr[i] < pvoit) {
      [arr[i], arr[lt + 1]] = [arr[lt + 1], arr[i]]
      lt++
      i++
    } else if (arr[i] > pvoit) {
      [arr[i], arr[gt - 1]] = [arr[gt - 1], arr[i]]
      gt--
    } else {
      i++
    }
  }

  [arr[l], arr[lt]] = [arr[lt], arr[l]]

  quickSortIn3Ways(arr, l, lt - 1)
  quickSortIn3Ways(arr, gt, r)
  return arr
}

function swapArr (arr, a, b) {
  [arr[a], arr[b]] = [arr[b], arr[a]]
}

let arr = [6, 2, 5, 1, 8, 2, 2, 10, 2, 6, 5, 9, 2, 7, 7, 9, 7, 0, 4, 5, 10, 1, 3, 3, 2, 5, 5, 9, 0, 4, 7, 2, 8, 9, 9, 3, 6, 9, 8, 10, 2,
  0, 2, 7, 10, 2, 3, 9, 4, 6, 7, 4, 7, 2, 8, 8, 4, 0, 3, 5, 2, 2, 9, 2, 5, 1, 4, 3, 10, 4, 2, 9, 4, 10, 4, 0, 0, 2, 1, 0, 5, 10
 , 9, 3, 2, 0, 8, 7, 5, 9, 5, 8, 2, 10, 3, 1, 5, 10, 4, 8, 9, 7, 10, 10, 10, 10, 7, 7, 3, 6, 4, 6, 6, 2, 4, 4, 4, 4, 2, 10, 5,
 6, 9, 3, 2, 1, 0, 9, 10, 10, 2, 6, 8, 7, 0, 0, 8, 9, 4, 6, 1, 5, 0, 10, 9, 5, 0, 0, 1, 7, 10, 1, 10, 7, 8, 1, 3, 8, 10, 1, 9,
 3, 10, 4, 0, 2, 4, 2, 9, 10, 0, 8, 0, 2, 10, 10, 2, 5, 5, 6, 1, 1, 9, 3, 3, 5, 6, 6, 9, 1, 1, 4, 7, 5, 9, 2, 2, 6, 7, 1]
quickSortIn3Ways(arr, 0, arr.length - 1)
