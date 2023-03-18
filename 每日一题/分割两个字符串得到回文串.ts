/* 给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。

当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。

如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。

注意， x + y 表示连接字符串 x 和 y 。

 

示例 1：

输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。
示例 2：

输入：a = "abdef", b = "fecab"
输出：true
示例 3：

输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。 */

function checkPalindromeFormation(a: string, b: string): boolean {
    // 检查a或b为回文串
    if (isPalindromic(a) || isPalindromic(b)) {
        return true;
    }
    // 如果是aprefix + bsuffix为回文串
    // 假设切割点为i
    
    return checkTwostr(a, b) || checkTwostr(b, a)

    // 如果是bprefix + asuffix为回文串
    // 假设切割点为i
}

function isPalindromic(str: string) {
    let i = 0;
    let j = str.length - 1;
    while (i < j) {
        if (str[i] !== str[j]) {
            return false;
        } else {
            i++
            j--
        }
    }
    return true;
}

function checkTwostr(a: string, b: string) {
    let i = 0;
    let lens = a.length - 1;
    while (i < lens - i && a[i] === b[lens - i]) {
        i++;
        // console.log(i)
    }
    if (i === lens - i) {
        return true;
    } else {
        const resPrefixA = a.slice(i, lens - i + 1);
        const resSuffixB = b.slice(i, lens - i + 1);
        // console.log(resPrefixA, resSuffixB)
        if (isPalindromic(resPrefixA) || isPalindromic(resSuffixB)) {
            return true;
        }
    }
    return false
}

console.log(checkPalindromeFormation('x', 'y'));
console.log(checkPalindromeFormation('abdef', 'fecab'));
console.log(checkPalindromeFormation("ulacfd", "jizalu"))
console.log(checkPalindromeFormation("ab", "cd"))
console.log(checkPalindromeFormation("abda", "acmc"))
// console.log(checkTwostr("abda", "acmc"))