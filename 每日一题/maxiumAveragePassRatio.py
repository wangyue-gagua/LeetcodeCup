""" There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
  """

from typing import List

import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]],
                        extraStudents: int) -> float:
        """贪心算法 利用heapq保存每个班的pass ratio, 每次取pass ratio最小的班级, 将其通过人数 + 1 总人数 + 1"""

        def get_ratio(passed, total):
            return (passed / total) - (passed + 1) / (total + 1)

        heap = []
        for passed, total in classes:
            heapq.heappush(heap, (get_ratio(passed, total), passed, total))



        # print("init", heap)

        for _ in range(extraStudents):
            ratio, passed, total = heapq.heappop(heap)
            # print(ratio, passed, total, heap)
            heapq.heappush(heap, (get_ratio(passed + 1, total + 1), passed + 1,
                                  total + 1))

        # print(heap)

        return sum(passed / total for _, passed, total in heap) / len(classes)


print(Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
print(Solution().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))


""" class Entry:
    __slots__ = 'p', 't'

    def __init__(self, p: int, t: int):
        self.p = p
        self.t = t

    def __lt__(self, b: 'Entry') -> bool:
        return (self.t - self.p) * b.t * (b.t + 1) > (b.t - b.p) * self.t * (self.t + 1)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [Entry(*c) for c in classes]
        heapify(h)
        for _ in range(extraStudents):
            heapreplace(h, Entry(h[0].p + 1, h[0].t + 1))
        return sum(e.p / e.t for e in h) / len(h)

作者：力扣官方题解
链接：https://leetcode.cn/problems/maximum-average-pass-ratio/solutions/2118606/zui-da-ping-jun-tong-guo-lu-by-leetcode-dm7y3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 

重写__lt__方法, 使得heapq可以按照自定义的规则进行排序
简化比较使得浮点运算变为整型运算。heapq.heapreplace()方法会将堆顶元素弹出并返回，同时将新元素插入堆中，更加有效。

"""