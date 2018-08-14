function mergeSort (arr) {
  if (arr.length === 1) {
    return arr;
  }

  let mid = Math.floor(arr.length / 2);
  let leftArr = arr.slice(0, mid);
  let rightArr = arr.slice(mid);

  // 分而治之的思想
  // 递归调用 mergeSort方法
  return merge(mergeSort(leftArr), mergeSort(rightArr))
}

function merge (left, right) {
  // 以空间换时间，新建了一个 result的变量
  let result = [];
  let il = 0;
  let ir = 0;

  while (il < left.length && ir < right.length) {
    if (left[il] < right[ir]) {
      result.push(left[il++]);
    } else {
      result.push(right[ir++]);
    }
  }

  while (il < left.length) {
    result.push(left[il++]);
  }

  while (ir < right.length) {
    result.push(right[ir++]);
  }

  return result;
}

console.log(mergeSort([3, 2, 6, 5, 4, 7, 1]))
