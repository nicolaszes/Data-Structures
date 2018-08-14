/**
 * binary search 非递归
 * @param arr 
 * @param target 
 */
function binarySearch (arr, target) {
  let l = 0
  let r = arr.length - 1

  while (l <= r) {
    let mid = Math.floor(l + (r - l + 1) / 2)

    if (arr[mid] === target) return mid

    if (arr[mid] < target) {
      l = mid + 1
    } else {
      r = mid - 1
    }
  }

  return -1
}

let arr = [-1,0,1,2,3,4,5,6,7,8,10,13,14,16,18,19,40]
binarySearch(arr, 16)


/**
 * use recurtion
 * @param {*} arr 
 * @param {*} index 
 * @param {*} target 
 */
function binarySearchByRecursion (arr, index, target) {
  let mid = Math.floor(arr.length / 2)

  if (mid == 0 && target != arr[mid])
    return -1

  if (arr[mid] < target) {
    return binarySearchByRecursion(arr.slice(mid), index + mid, target)
  }
  if (arr[mid] > target) {
    return binarySearchByRecursion(arr.slice(0, mid), index, target)
  } 
  return index + mid
}

let arr = [-1,0,1,2,3,4,5,6,7,8,10,13,14,16,18,19,40]
binarySearchByRecursion(arr, 0, 16)