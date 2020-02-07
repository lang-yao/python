# -*- coding: utf-8 -*-
# @Time    : 19/11/29 23:21
# @Author  : sloth
# @File    : good_number.py


# 回环
def cmp(s1, s2):
    # 求两个字符串的最长公共子串
    # 思想：建立一个二维数组，保存连续位相同与否的状态

    len_s1 = len(s1)
    len_s2 = len(s2)

    # 生成0矩阵，为方便后续计算，多加了1行1列
    # 行: (len_s1+1)
    # 列: (len_s2+1)
    record = [[0 for i in range(len_s2 + 1)] for j in range(len_s1 + 1)]

    maxNum = 0  # 最长匹配长度
    p = 0  # 字符串匹配的终止下标

    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                # 相同则累加
                record[i + 1][j + 1] = record[i][j] + 1

                if record[i + 1][j + 1] > maxNum:
                    maxNum = record[i + 1][j + 1]
                    p = i  # 匹配到下标i

    # 返回 子串长度，子串
    return maxNum, s1[p + 1 - maxNum: p + 1]


# 重复
def main():
    phones = []
    with open('phones', 'r') as f:
        phones = f.readlines()
    res = []
    cl = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999', '000']
    for num in phones:
        a, b = cmp(num, num[::-1])
        if a > 3:
            print(a, num, end='')
            continue
        for i in cl:
            if i in num:
                print(i, num)


if __name__ == '__main__':
    # a, b = cmp('15890101352', '25310109851')
    # print(a, b)
    main()
