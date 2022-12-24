// function sum() {
//     let args = Array.from(arguments);
//     let fn = function () {
//         args.push(...arguments);
//         return fn;
//     };
//     fn.call = function () {
//         return args.reduce((a, b) => a + b);
//     };
//     return fn;
// }

// function mySum() {
//     let args = Array.from(arguments);
//     let fn = function () {
//         args.push(...arguments);
//         return fn;
//     };
//     fn.call = function () {
//         return args.reduce((a, b) => a + b);
//     };
//     if (args.length === 0) return fn.call();
//     return fn;
// }



// console.log(mySum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)(2)());
// console.log(sum(1, 2, 3)().call());
// console.log(sum(1)(2)(3)());
// console.log(sum(1, 2)(3)());
// console.log(sum(1)(2, 3)());

function anOtherSum(func) {

    return function curried(...args) {
      if (args.length >= func.length) {
        return func.apply(this, args);
      } else {
        return function(...args2) {
          return curried.apply(this, args.concat(args2));
        }
      }
    };
  
  }

function sum(a, b, c) {
    return a + b + c;
}

let curriedSum = anOtherSum(sum);
console.log(curriedSum(1, 2)(3)(4));