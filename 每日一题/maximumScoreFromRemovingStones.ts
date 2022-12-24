/* You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get. */

function maximumScore(a: number, b: number, c: number): number {
    const arr = [a, b, c];
    arr.sort((a, b) => a - b);
    let [a1, b1, c1] = arr;
    if (a1 + b1 <= c1) {
        return a1 + b1;
    } else {
        return Math.floor((a1 + b1 + c1) / 2);
    }
};