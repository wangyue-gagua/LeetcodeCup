from typing import List


def checkIsPossibleStackSequence(sIn: List[int], sOut: List[int]):
    """判断sIn是否可以通过栈的方式得到sOut"""
    if len(sIn) != len(sOut):
        return False
    stack = []
    i = 0
    j = 0
    while i < len(sIn):
        if len(stack) > 0 and stack[-1] == sOut[j]:
            stack.pop()
            j += 1
        else:
            stack.append(sIn[i])
            i += 1
    while len(stack) > 0:
        if stack[-1] == sOut[j]:
            stack.pop()
            j += 1
        else:
            return False
    return True


T = int(input())
for i in range(T):
    n = int(input())
    sIn = [int(i) for i in input().split()]
    sOut = [int(i) for i in input().split()]
    if checkIsPossibleStackSequence(sIn, sOut):
        print("Yes")
    else:
        print("No")
