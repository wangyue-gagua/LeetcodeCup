/* Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order. */

/**
 * @param {string} s
 * @return {string[]}
 */
 var letterCasePermutation = function(s) {
    const len = s.length;
    let backTrace = (index, path) => {
        if (index === len - 1) {
            result.push(path);
            return;
        }
        for (let i = index; i < s.length; i++) {
            let char = s[i];
            if (char.match(/[a-z]/i)) {
                backTrace(i + 1, path + char.toLowerCase());
                backTrace(i + 1, path + char.toUpperCase());
            } else {
                backTrace(i + 1, path + char);
            }
        }
    }
    let result = [];
    backTrace(0, '');
    return result;
};

console.log(letterCasePermutation('a1b2'));