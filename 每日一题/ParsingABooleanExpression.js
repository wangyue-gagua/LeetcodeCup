/* A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false. */

/**
 * @param {string} expression
 * @return {boolean}
 */
 var parseBoolExpr = function(expression) {
    const bracketStack = []
    const valueStack = []
    let val = []
    for (let i of expression) {
        if (i === "(") {
            bracketStack.push("(")
        } else if (i === ")") {
            while (true) {
                // console.log(valueStack)
                let lastVal = valueStack.pop()
                if ([false, true].includes(lastVal)) {
                    val.push(lastVal)
                } else {
                    // console.log(valueStack, lastVal)
                    if (lastVal === "!") {
                        // console.log("val: ", val)
                        valueStack.push(!val[0])
                        val = []
                        
                    } else if (lastVal === "&") {
                        valueStack.push(!val.includes(false))
                        val = []
                    } else {
                        valueStack.push(val.includes(true))
                        val = []
                    }
                    // console.log(valueStack)
                    break
                }
            }
        } else if (i === ",") {
            continue
        } else if (["&", "|", "!"].includes(i)) {
            valueStack.push(i)
        } else {
            valueStack.push(i === "t")
        }
    }
    return valueStack[0]

};

console.log(parseBoolExpr("&(|(f))"))