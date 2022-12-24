
/* You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick. */

/**
 * @param {number[]} fruits
 * @return {number}
 */
 var totalFruit = function(fruits) {
// slide window
// keep track of the last two types of fruit
// if the current fruit is not one of the last two types, then we need to move the window
// if the current fruit is one of the last two types, then we can keep the window
// keep track of the max number of fruits we can pick
// return the max number of fruits we can pick
    let max = 0;
    let lastTwo = new Map();
    let windowStart = 0;
    for (let windowEnd = 0; windowEnd < fruits.length; windowEnd++) {
        let currentFruit = fruits[windowEnd];
        if (!lastTwo.has(currentFruit)) {
            lastTwo.set(currentFruit, 1);
        } else {
            lastTwo.set(currentFruit, lastTwo.get(currentFruit) + 1);
        }
        while (lastTwo.size > 2) {
            let fruitToRemove = fruits[windowStart];
            lastTwo.set(fruitToRemove, lastTwo.get(fruitToRemove) - 1);
            if (lastTwo.get(fruitToRemove) === 0) {
                lastTwo.delete(fruitToRemove);
            }
            windowStart++;
        }
        max = Math.max(max, windowEnd - windowStart + 1);
    }
    return max;
};

console.log(totalFruit([0,1,2,2]))