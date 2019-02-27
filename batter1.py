#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:42:38 2019

@author: matsuoseikou
"""


"""毎回の打席でprob(.250)の確率で必ずヒットを打つ打者がいたとき
彼がシーズンn(500)打数立つことをm(1000)回行った時に打率av(.300)を記録する確率"""

import numpy as np
import matplotlib.pyplot as plt



def batter(prob=0.25, av=0.3, n=500, m=1000):
    l = []#リスト
    count = 0#カウンター
    for _ in range(m):#m回の試行
        x = np.random.random(n)#0~1の乱数をn個生成(500打数の結果)
        a = np.sum(x<=prob)#prob以下の要素を数える（安打数)
        p = a/n#割合に変換(打率)
        if p >= av:#打率がavを超える数を数える
            count += 1
        l.append(p)#各打率をリストに追加
        poss = count/#m回の試行で打率がavを超えた割合
    return l, poss

a,b = batter()
plt.hist(a)
plt.show()
print(b)



            
        