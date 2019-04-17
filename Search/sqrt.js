/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 0 || typeof(x) !== 'number') {
        return false
    }
    if (x === 0 || x === 1) {
        return x
    }
    let l = 0
    let r = x
    while (l <= r) {
        let mid = Math.floor(l + ((r - l) / 2))
        console.log(mid)
        if (r - l <= 1) {
            return mid
        }
        if (mid * mid === x) {
            return mid
        }
        if (mid * mid > x) {
            r = mid
        } else {
            l = mid
        }
    }
};