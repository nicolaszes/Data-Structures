function swap(array, a, b) {
  [array[a], array[b]] = [array[b], array[a]]
}

class MinHeap {
  heap = []
  getLeftIndex(index) {
    return (2 * index) + 1
  }

  getRightIndex(index) {
    return (2 * index) + 2
  }

  getParentIndex(index) {
    if (index === 0) {
      return undefined
    }
    return Math.floor((index - 1) / 2)
  }

  size() {
    return this.heap.length
  }

  isEmpty() {
    return this.size() <= 0
  }

  insert(value) {
    if (value != null) {
      const index = this.size()
      this.heap.push(value)
      this.siftUp(index)
      return true
    }
    return false
  }

  siftDown(index) {
    let element = index
    const left = this.getLeftIndex(index)
    const right = this.getRightIndex(index)
    const size = this.size()
    if (left < size && this.heap[element] > this.heap[left]) {
      element = left
    }
    if (right < size && this.heap[element] > this.heap[right]) {
      element = right
    }
    if (index !== element) {
      swap(this.heap, index, element)
      this.siftDown(element)
    }
  }

  siftUp(index) {
    let parent = this.getParentIndex(index)
    while (index > 0 && this.heap[parent] > this.heap[index]) {
      swap(this.heap, parent, index)
      index = parent
      parent = this.getParentIndex(index)
    }
  }
}

var findKthLargest = function (nums, k) {
  var res = new MinHeap()
  for (var i = 0, len = nums.length; i < len; i++) {
    if (i < k) {
      res.insert(nums[i])
    } else {
      if (nums[i] >= res.heap[0]) {
        res.heap[0] = nums[i]
        res.siftDown(0)
      }
    }
  }
  return res.heap[0]
}

/**
 * 分治
 * @param {*} arr 
 * @param {*} left 
 * @param {*} right 
 */
function partition(arr, left, right) {
  if (right > left) {
      var randomIndex = Math.floor(Math.random() * (right - left + 1) + left);
      [arr[left], arr[randomIndex]] = [arr[randomIndex], arr[left]]
  }

  var pivot = arr[left];
  var j = left;
  for (var i = left + 1; i <= right; i++) {
      if (arr[i] < pivot) {
          // 小于 pivot 的元素都被交换到前面
          j++;
          [arr[i], arr[j]] = [arr[j], arr[i]]
      }
  }
  // 在之前遍历的过程中，满足 [left + 1, j] < pivot，并且 (j, i] >= pivot
  [arr[j], arr[left]] = [arr[left], arr[j]]
  // 交换以后 [left, j - 1] < pivot, nums[j] = pivot, [j + 1, right] >= pivot
  return j;
}

var findKthLargest = function (nums, k) {
  var len = nums.length;
  var left = 0;
  var right = len - 1;

  // 转换一下，第 k 大元素的索引是 len - k
  var target = len - k;

  while (left <= right) {
      var index = partition(nums, left, right);
      if (index == target) {
          return nums[index];
      } else if (index < target) {
          left = index + 1;
      } else {
          right = index - 1;
      }
  }
};