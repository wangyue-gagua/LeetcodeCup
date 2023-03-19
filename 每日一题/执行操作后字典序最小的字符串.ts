/* 给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。

你可以在 s 上按任意顺序多次执行下面两个操作之一：

累加：将  a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。
轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。

如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。

 

示例 1：

输入：s = "5525", a = 9, b = 2
输出："2050"
解释：执行操作如下：
初态："5525"
轮转："2555"
累加："2454"
累加："2353"
轮转："5323"
累加："5222"
累加："5121"
轮转："2151"
累加："2050"​​​​​​​​​​​​
无法获得字典序小于 "2050" 的字符串。
示例 2：

输入：s = "74", a = 5, b = 1
输出："24"
解释：执行操作如下：
初态："74"
轮转："47"
累加："42"
轮转："24"​​​​​​​​​​​​
无法获得字典序小于 "24" 的字符串。
示例 3：

输入：s = "0011", a = 4, b = 2
输出："0011"
解释：无法获得字典序小于 "0011" 的字符串。
示例 4：

输入：s = "43987654", a = 7, b = 3
输出："00553311" */

function findLexSmallestString(s: string, a: number, b: number): string {
    // 当b为偶数时，轮转不能影响被加数
    // 枚举所有轮转可能

    const allPossibleRotates = generateAllRotate(s, b);
    console.log("rotate", allPossibleRotates);
    let minStr = s;
    for (let rotate of allPossibleRotates) {
        let allPossibleAdds: Set<string> = new Set();
        if (b % 2 === 0) {
            allPossibleAdds = strAdd(rotate, a, false);
        } else {
            allPossibleAdds = strAdd(rotate, a, true);
        }
        for (let add of allPossibleAdds) {
            if (add < minStr) {
                minStr = add;
            }
        }
    }
    return minStr;
}

function generateAllRotate(s: string, b: number) {
    const res: Set<string> = new Set();
    // b为奇数时，所有字符都能成为首位
    // b为偶数时，只有偶数位的字符能成为首位
    // 无论奇偶其实都不能保证所有字符都能成为首位
    for (let i = 0; i < s.length; i = (b + i) % s.length) {
        const temp = s.slice(i) + s.slice(0, i);
        if (res.has(temp)) {
            break;
        } else {
            res.add(temp);
        }
    }

    return res;
}

function strAdd(s: string, a: number, isOdd: boolean) {
    // 对s中的奇数位进行累加
    const res: Set<string> = new Set();
    let curA = a;
    while (true) {
        let tempRes = [];
        for (let i = 0; i < s.length; i++) {
            if (i % 2 === 0) {
                tempRes.push(s[i]);
                continue;
            }
            let curPointVal = (parseInt(s[i]) + curA) % 10;
            tempRes.push(curPointVal.toString());
        }
        if (res.has(tempRes.join(""))) {
            break;
        } else {
            res.add(tempRes.join(""));
        }
        curA += a;
    }
    if (isOdd) {
        // 对奇数位所有可能分别对偶数位进行累加
        const tempRes: Set<string> = new Set(res);
        for (let str of res) {
            let curA = a;
            while (true) {
                let tempRes2 = [];
                for (let i = 0; i < str.length; i++) {
                    if (i % 2 === 1) {
                        tempRes2.push(str[i]);
                        continue;
                    }
                    let curPointVal = (parseInt(str[i]) + curA) % 10;
                    tempRes2.push(curPointVal.toString());
                }
                if (tempRes.has(tempRes2.join(""))) {
                    break;
                } else {
                    tempRes.add(tempRes2.join(""));
                }
                curA += a;
            }
        }
        return tempRes.add(s);
    }
    return res;
}

// console.log(generateAllRotate("5525", 1));
// console.log(strAdd("1234", 4));

// console.log(findLexSmallestString("5525", 9, 2));
// console.log(findLexSmallestString("74", 5, 1));
// console.log(findLexSmallestString("0011", 4, 2));
// console.log(findLexSmallestString("43987654", 7, 3));

// console.log(generateAllRotate("43987654", 3))

// console.log(strAdd('44398765', 7, true))

// console.log(findLexSmallestString("593290172167", 7, 4));
// console.log(generateAllRotate("593290172167", 4));

// console.log(findLexSmallestString("192804", 8, 5))
// console.log(generateAllRotate("192804", 5))

// console.log(findLexSmallestString("58016941393090", 9, 6))

// console.log(findLexSmallestString("87144140372271458627", 4, 8));

console.log(findLexSmallestString("863376891476", 4, 9));
