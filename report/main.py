# -*- coding: utf-8 -*-
# author  : sloth
# file    : main.py
# time    : 2020/1/30 10:30

import json, functools


def call_msg(name):
    def msg(func):
        def wrapper(filename):
            func(filename)
            data = {}
            with open('top_attack/' + filename + '/2.txt') as f:
                data = f.read()
                data = json.loads(data)['data']
            data['highNum'] = data['fatalNum'] + data['highNum']
            print('total:\t', data['total'])
            print('high:\t', data['highNum'])
            print('midium:\t', data['middleNum'])
            print('low:\t', data['lowNum'])

            return data

        return wrapper

    return msg


@call_msg('zhengwu')
def zhengwu(filename):
    print('zhengwu')


@call_msg('renmin')
def renmin(filename):
    print('renmin')


@call_msg('shouxin')
def shouxin(filename):
    print('shouxin')


def zhengwu_2():
    data = {}
    with open('top_attack/zhengwu/_2.txt') as f:
        data = f.read()
        data = json.loads(data)
    count = {}
    count['total'] = data['total']
    data = data['data']['counts']
    for i in range(1, 10):
        if not data.get(str(i)):
            data[str(i)] = 0
    count['lowNum'] = data['2'] + data['3']
    count['middleNum'] = data['4'] + data['5']
    count['highNum'] = data['6'] + data['7'] + data['8'] + data['9']
    print('NGSOC区域：')
    print('total:\t', count['total'])
    print('high:\t', count['highNum'])
    print('midium:\t', count['middleNum'])
    print('low:\t', count['lowNum'])
    return count


def total_num():
    coutnt = zhengwu_2()
    data1 = zhengwu('zhengwu')
    data2 = renmin('renmin')
    data3 = shouxin('shouxin')
    total = {}

    total['highNum'] = data1['highNum'] + data2['highNum'] + data3['highNum'] + coutnt['highNum']
    total['middleNum'] = data1['middleNum'] + data2['middleNum'] + data3['middleNum'] + coutnt['middleNum']
    total['lowNum'] = data1['lowNum'] + data2['lowNum'] + data3['lowNum'] + coutnt['lowNum']
    total['total'] = data1['total'] + data2['total'] + data3['total'] + coutnt['total']

    return total


def top(name, file):
    def msg(func):
        def wrapper(filename):
            func(filename)
            data = {}
            with open('top_attack/' + filename + '/' + file) as f:
                data = f.read().encode('utf-8').decode('unicode_escape')
                data = json.loads(data)['data']
            data = sorted(data, key=functools.cmp_to_key(dict_cmp))
            for i, ct in zip(data, range(5)):
                print(i)
                if ct > 4:
                    break
            return data

        return wrapper

    return msg


@top('zhengwu', '1.txt')
def zhengwu_top(filename):
    print('zhengwu')


@top('zhengwu', '_1.txt')
def zhengwu_top_2(filename):
    print('zhengwu—-NGSOC')
    filename = 'top_attack/zhengwu/_1.txt'
    val = ''
    with open(filename, 'r') as f:
        val = f.read()
        val = val.replace('count', 'value')
    with open(filename, 'w') as f:
        f.write(val)


@top('renmin', '1.txt')
def renmin_top(filename):
    print('renmin')


@top('shouxin', '1.txt')
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
    data_NG = zhengwu_top_2('zhengwu')
    data1 = zhengwu_top('zhengwu')
    data = merge(data1, data_NG)
    print('政务区域TOP5：')
    for i, ct in zip(sorted(data, key=data.__getitem__, reverse=True), range(5)):
        if ct < 5:
            print(i + '\t' + str(data[i]))
    data2 = renmin_top('renmin')
    data3 = shouxin_top('shouxin')
    data = merge(data1, data2, data3, data_NG)
    print('所有区域TOP5：')
    for i, ct in zip(sorted(data, key=data.__getitem__, reverse=True), range(5)):
        if ct < 5:
            print(i + '\t' + str(data[i]))


def main():
    print('总计：\t', total_num())
    top5()


if __name__ == '__main__':
    main()
