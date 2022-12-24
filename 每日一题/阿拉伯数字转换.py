"""
通过函数将阿拉伯数字转换为中文
12345 一万两千三百四十五
"""

import sys

inString = 12304


def toChinese(num):
    yiNum = num // 100000000
    wanNum = num % 100000000 // 10000
    qianNum = num % 10000 // 1000
    baiNum = num % 1000 // 100
    shiNum = num % 100 // 10
    geNum = num % 10

    arabChineseMap = {
        0: '零',
        1: '一',
        2: '二',
        3: '三',
        4: '四',
        5: '五',
        6: '六',
        7: '七',
        8: '八',
        9: '九',
    }

    res = ''
    if yiNum > 0:
        res += toChinese(yiNum) + '亿'
    if wanNum != 0 and wanNum < 10:
        res += arabChineseMap[wanNum] + '万'
    if qianNum < 10:
        res += arabChineseMap[qianNum] + '千'
    if baiNum < 10:
        res += arabChineseMap[baiNum] + '百'
    if shiNum < 10:
        res += arabChineseMap[shiNum] + '十'
    if geNum != 0:
        res += arabChineseMap[geNum]
    return res


print(toChinese(inString))
