/* You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

There must be exactly one ice cream base.
You can add one or more types of topping or have no toppings at all.
There are at most two of each type of topping.
You are given three inputs:

baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
target, an integer representing your target price for dessert.
You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are multiple, return the lower one. */

function closestCost(baseCosts: number[], toppingCosts: number[], target: number): number {
    toppingCosts.sort((a, b) => a - b);
    const allPossibleCombination:number[] = []
    for(const num of toppingCosts) {
        if (allPossibleCombination.length === 0) {
            allPossibleCombination.push(0);
            allPossibleCombination.push(num)
            allPossibleCombination.push(num * 2)
        } else {
            const temp:number[] = []
            for(const num2 of allPossibleCombination) {
                temp.push(num2 + num)
                temp.push(num2 + num * 2)
            }
            allPossibleCombination.push(...temp)
        }
    }
    allPossibleCombination.sort((a, b) => a - b)
    // console.log(allPossibleCombination)
    const binarySearch = (target:number, arr:number[]) => {
        let left = 0
        let right = arr.length - 1
        while(left <= right) {
            const mid = Math.floor((left + right) / 2)
            if (arr[mid] === target) return mid
            if (arr[mid] > target) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return left
    }
    let res = 100000000
    for (const num of baseCosts) {
        const differenceVal = target - num
        if (differenceVal < 0) {
            const diff = Math.abs(num - target)
            if (diff < Math.abs(res - target)) {
                res = num
            }
        } else {
            const index = binarySearch(differenceVal, allPossibleCombination)
            // console.log(index)
            if (index === allPossibleCombination.length) {
                const curVal = num + allPossibleCombination[index - 1]
                const diff = Math.abs(curVal - target)
                if (diff <= Math.abs(res - target)|| diff === Math.abs(res - target)  && curVal <= res) {
                    res = curVal
                }
            } else {
                const curVal = num + allPossibleCombination[index]
                const diff = Math.abs(curVal - target)
                if (diff < Math.abs(res - target)|| diff === Math.abs(res - target)  && curVal <= res) {
                    res = curVal
                }
                if (index > 0) {
                    const curVal = num + allPossibleCombination[index - 1]
                    const diff = Math.abs(curVal - target)
                    if (diff <= Math.abs(res - target)) {
                        res = curVal
                    }
                }
            }
        }
    }
    // console.log(allPossibleCombination[59048])
    return res
};

console.log(closestCost([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10], 1000))