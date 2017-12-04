function countSort (listA) {
  c = [];
  res = [];

  for (let i = 0; i < 100; i++) {
    c.push(0);
  }

  for (let i = 0; i < listA.length; i++) {
    c[listA[i]] = c[listA[i]] + 1;
    res.push(0);
  }

  for (let i = 0; i < 100; i++) {
    c[i] = i === 0 ? c[i] : c[i - 1] + c[i];
  }

  for (let i = listA.length - 1; i > -1; i--) {
    res[c[listA[i]] - 1] = listA[i];
    c[listA[i]] = c[listA[i]] - 1;
  }


  return res;
}

newArr = [2, 3, 4, 1, 5, 6, 7, 2, 3]
console.log(countSort(newArr))
