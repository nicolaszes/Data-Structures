/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  if (!Array.isArray(triangle)) {
    return 0
  }

  let res = triangle
  for (let i = triangle.length - 2; i > -1; i--) {
    for (let j = 0; j < triangle[i].length; j++) {
      res[i][j] = Math.min(res[i + 1][j], res[i + 1][j + 1]) + triangle[i][j]
    }
  }
  return res[0][0]
};