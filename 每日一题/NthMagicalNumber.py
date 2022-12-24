""" A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
  """

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        def lcm(a, b):
            return a * b // gcd(a, b)
        mod = 10 ** 9 + 7
        l = lcm(a, b)
        low, high = min(a, b), n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            if mid // a + mid // b - mid // l < n:
                low = mid + 1
            else:
                high = mid
        return low % mod