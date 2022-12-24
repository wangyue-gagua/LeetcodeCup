"""
给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：

删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
请你返回纸上能写出的字典序最小的字符串。

示例 1：

输入：s = "zza"
输出："azz"
解释：用 p 表示写出来的字符串。
一开始，p="" ，s="zza" ，t="" 。
执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
"""

from collections import deque


class Solution:
    def robotWithString(self, s: str) -> str:
        res = ""
        stack = []
        queue = deque(s)
        memoryS = [(n, i) for i, n in enumerate(s)]
        memoryS.sort()
        memoryS = deque(memoryS)
        minChar = ""
        index = 0
        while queue or stack:
            if not queue:
                res += stack.pop()
            elif not stack:
                while memoryS:
                    if memoryS[0][1] < index:
                        memoryS.popleft()
                    else:
                        minChar = memoryS[0][0]
                        index = memoryS[0][1]
                        memoryS.popleft()
                        break
                for i in range(index):
                    stack.append(queue.popleft())
                res += queue.popleft()
            else:
                while memoryS:
                    if memoryS[0][1] < index:
                        memoryS.popleft()
                    else:
                        minChar = memoryS[0][0]
                        index = memoryS[0][1]
                        memoryS.popleft()
                        break
                if minChar < stack[-1]:
                    for i in range(index):
                        stack.append(queue.popleft())
                        print(stack, queue, res, memoryS)
                    res += queue.popleft()
                else:
                    res += stack.pop()
        return res

from typing import Deque


class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()
        
        for i in range(26):
            d[i] = 0
        
        ans = ''
        
        for v in s:
            v = ord(v) - ord('a')
            d[v] += 1
        
        stack = Deque()
        for v in s:
            v = ord(v) - ord('a')
            stack.append(v)
            d[v] -= 1
            
            while len(stack) > 0:
                x = stack[-1]
                flag = 1
                for i in range(x):
                    if d[i] > 0:
                        flag = 0
                if flag:
                    ans += chr(97+stack[-1])
                    stack.pop()
                else:
                    break
        
        while len(stack) > 0:
            ans += chr(97+stack[-1])
            stack.pop()
        
        return ans
                


print(Solution().robotWithString("bac"))