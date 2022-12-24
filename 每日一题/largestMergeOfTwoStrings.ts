/* You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c. */

function largestMerge(word1: string, word2: string): string {
    let index1 = 0;
    let index2 = 0;
    let res = '';
    while (index1 < word1.length && index2 < word2.length) {
        if (word1[index1] > word2[index2]) {
            res += word1[index1];
            index1++;
        } else if (word1[index1] < word2[index2]) {
            res += word2[index2];
            index2++;
        } else {
            // word1[index1] === word2[index2]
            let temp1 = index1;
            let temp2 = index2;
            while (temp1 < word1.length && temp2 < word2.length && word1[temp1] === word2[temp2]) {
                temp1++;
                temp2++;
            }
            if (temp1 === word1.length) {
                res += word2[index2];
                index2++;
            } else if (temp2 === word2.length) {
                res += word1[index1];
                index1++;
            } else {
                if (word1[temp1] > word2[temp2]) {
                    res += word1[index1];
                    index1++;
                } else {
                    res += word2[index2];
                    index2++;
                }
            }
        }
    }
    if (index1 < word1.length) {
        res += word1.slice(index1);
    }
    if (index2 < word2.length) {
        res += word2.slice(index2);
    }
    return res;
};

console.log(largestMerge('cabaa', 'bcaaa'));
console.log(largestMerge('abcabc', 'abdcaba'));