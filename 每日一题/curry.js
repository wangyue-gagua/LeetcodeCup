// 柯里化
function curry(fn) {
    return function curried(...args) {
        if (args.length < fn.length) {
            return function() {
                return curried(...args.concat(Array.from(arguments)))
            }
        }
        return fn(...args)
    }
}

// curry sum
function sum(a, b, c) {
    return a + b + c
}

const curriedSum = curry(sum)
console.log(curriedSum(1, 2, 3))
console.log(curriedSum(1)(2, 3))
console.log(curriedSum(1)(2)(3))
