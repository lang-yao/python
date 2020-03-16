# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 8:59
# @Author  : sloth
# @File    : book_del_biaozhu.py


if __name__ == '__main__':
    def get_line():
        for i in open('in.txt', 'r', encoding='utf-8'):
            i = i.replace(' ', '')
            i = i.replace('　', '')
            if i.find(u'标注') == -1:
                yield i


    open('res.txt', 'w', encoding='utf-8').write(''.join(get_line()))
