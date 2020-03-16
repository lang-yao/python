# -*- coding: utf-8 -*-
# author  : sloth
# file    : main.py
# time    : 2020/1/30 10:30

import json, functools


def top(name):
    def msg(func):
        def wrapper(filename):
            func(filename)
            data = {}
            with open(filename + '.txt') as f:
                data = f.read().encode('utf-8').decode('unicode_escape')
                data = json.loads(data)['data']
            data = sorted(data, key=functools.cmp_to_key(dict_cmp))
            for i, ct in zip(data, range(5)):
                print(i)
            return data

        return wrapper

    return msg


@top('zhengwu')
def zhengwu_top(filename):
    print('zhengwu')


@top('renmin')
def renmin_top(filename):
    print('renmin')


@top('shouxin')
def shouxin_top(filename):
    print('shouxin')


def merge(*args):
    data = {}
    for i in args:
        for dic in i:
            if data.get(dic['name']):
                data[dic['name']] += dic['value']
            else:
                data[dic['name']] = dic['value']
    return data


def dict_cmp(dict1, dict2):
    if dict1['value'] > dict2['value']:
        return -1
    if dict1['value'] < dict2['value']:
        return 1
    return 0


def top5():
    data1 = zhengwu_top('zhengwu')
    data2 = renmin_top('renmin')
    data3 = shouxin_top('shouxin')
    data = merge(data1, data2, data3)
    for i, ct in zip(sorted(data, key=data.__getitem__, reverse=True), range(5)):
        if ct < 5:
            print(i + '\t' + str(data[i]))


def main():
    top5()


if __name__ == '__main__':
    main()
