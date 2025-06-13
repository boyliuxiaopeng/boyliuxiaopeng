# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 21:05:35 2020.

@author: Lenovo.
arm:多项式操作.
requirement:求多项式函数 y = a* x ** 3 + b * x ** 2 +c*x + d的驻点.

"""

import numpy as np
import matplotlib.pyplot as plt

def nums(a,b,c,d,e,f):
    """定义递归."""
    n = 1000
    x = np.linspace(e, f, n + 1)
    x1 = np.linspace(e, f, n + 1)

    y = a * x ** 3 + b * x ** 2 + c * x + d
    #plt.xlim([-100,50])
    #plt.ylim([-800,50])
    plt.plot(x1, y,ls='--')

    # 求多项式函数的导函数
    P = [a, b, c, d]
    Q = np.polyder(P)
    # 得到驻点的横坐标
    xs = np.roots(Q)
    print(xs)
    # 将横坐标带入多项式函数，得到纵坐标
    # 计算多项式的函数值。返回在xs处多项式的值，p为多项式系数，元素按多项式降幂排序。
    Y = np.polyval(P, xs)
    print(Y)
    #plt.plot(x, y, ls='--', c='deeppink', label='')
    plt.scatter(xs, Y, s=20, color='red', marker='o', zorder=3)
    #plt.plot(x, y,ls='--')
    plt.show()

if __name__ == "__main__":
    '''3阶多项式系数，区间'''
    nums(-0.00633705,0.329678442,-5.30186574,13.4924393,17.1,23.8)
