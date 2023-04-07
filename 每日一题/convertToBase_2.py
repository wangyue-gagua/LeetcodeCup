""" Given an integer n, return a binary string representing its representation in base -2.

Note that the returned string should not have leading zeros unless the string is "0".

 

Example 1:

Input: n = 2
Output: "110"
Explantion: (-2)2 + (-2)1 = 2
Example 2:

Input: n = 3
Output: "111"
Explantion: (-2)2 + (-2)1 + (-2)0 = 3
Example 3:

Input: n = 4
Output: "100"
Explantion: (-2)2 = 4
 

Constraints:

0 <= n <= 109 """

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        while n:
            ans = str(n % 2) + ans
            n =  -(n //2)
            print(n)
        return ans
    
# print(Solution().baseNeg2(2))
# print(Solution().baseNeg2(3))
print(Solution().baseNeg2(4))
print((1 // -2))