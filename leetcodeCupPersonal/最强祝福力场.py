""" 小扣在探索丛林的过程中，无意间发现了传说中“落寞的黄金之都”。而在这片建筑废墟的地带中，小扣使用探测仪监测到了存在某种带有「祝福」效果的力场。
经过不断的勘测记录，小扣将所有力场的分布都记录了下来。forceField[i] = [x,y,side] 表示第 i 片力场将覆盖以坐标 (x,y) 为中心，边长为 side 的正方形区域。

若任意一点的 力场强度 等于覆盖该点的力场数量，请求出在这片地带中 力场强度 最强处的 力场强度。

注意：

力场范围的边缘同样被力场覆盖。
示例 1：

输入：
forceField = [[0,0,1],[1,0,1]]

输出：2

解释：如图所示，（0.5, 0) 处力场强度最强为 2， （0.5，-0.5）处力场强度同样是 2。
image.png

示例 2：

输入：
forceField = [[4,4,6],[7,5,3],[1,6,2],[5,6,3]]

输出：3

解释：如下图所示，
forceField[0]、forceField[1]、forceField[3] 重叠的区域力场强度最大，返回 3
image.png

提示：

1 <= forceField.length <= 100
forceField[i].length == 3
0 <= forceField[i][0], forceField[i][1] <= 10^9
1 <= forceField[i][2] <= 10^9 """

from typing import List


class Solution:
    def fieldOfGreatestBlessing(self, forceField: List[List[int]]) -> int:
        # 拆分区域，并维护每个区域的力场数量

        # 对于每个四边形区域，维护左下角坐标以及宽高和当前区域立场数 area = [x, y, w, h, count]

        def transform(x, y, side):
            # 将力场转换为区域
            return [x - side / 2, y - side / 2, side, side, 1]
        
        def calAreaOverlap(area1, area2):
            # 计算两个区域的重叠区域
            x1, y1, w1, h1, c1 = area1
            x2, y2, w2, h2, c2 = area2
            x = max(x1, x2)
            y = max(y1, y2)
            w = min(x1 + w1, x2 + w2) - x
            h = min(y1 + h1, y2 + h2) - y
            if w >= 0 and h >= 0:
                return [x, y, w, h, c1 + c2]
            else:
                return None
            
        # 对每个立场两两计算重叠区域
        res = 1
        areas = []
        for i, f in enumerate(forceField):
            transformedArea = transform(*f)
            newAreas = [transformedArea]
            for area in areas:
                overlap = calAreaOverlap(transformedArea, area)
                if overlap:
                    newAreas.append(overlap)
                    res = max(res, overlap[4])
            areas.extend(newAreas)
            # print(len(areas))
        return res
            
            

        

    
print(Solution().fieldOfGreatestBlessing([[0,0,1],[1,0,1]]))
print(Solution().fieldOfGreatestBlessing([[4,4,6],[7,5,3],[1,6,2],[5,6,3]]))

print(Solution().fieldOfGreatestBlessing([[7,7,9],[7,5,3],[1,8,5],[5,6,3],[9,10,2],[8,4,10]]))

# test = [[932,566,342],[546,489,250],[723,454,748],[830,887,334],[617,534,721],[924,267,892],[151,64,65],[318,825,196],[102,941,940],[748,562,582],[76,938,228],[921,15,245],[871,96,823],[701,737,991],[339,861,146],[484,409,823],[574,728,557],[104,845,459],[363,804,94],[445,685,83],[324,641,328],[626,2,897],[656,627,521],[935,506,956],[210,848,502],[990,889,112]]
# print(Solution().fieldOfGreatestBlessing(test))

# test2 = [[502,549,472],[261,467,508],[722,915,742],[488,333,449],[221,262,49],[346,30,940],[273,535,829],[44,46,423],[45,195,506],[54,378,472],[167,83,451],[359,215,121],[4,891,88],[297,538,84],[671,355,247],[8,193,102],[144,858,847],[66,207,784],[806,258,158],[439,689,424],[697,747,906],[228,754,942],[994,309,219],[624,320,452],[407,530,628],[572,881,79],[944,394,838],[227,261,438],[465,494,573],[198,353,773],[348,893,908],[623,730,850],[105,246,404],[621,46,41],[905,314,982],[88,957,185],[814,566,256],[327,75,502],[331,10,226]]
# # print(len(test2))
# print(Solution().fieldOfGreatestBlessing(test2))