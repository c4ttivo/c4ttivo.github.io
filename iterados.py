# -*- coding: utf-8 -*-
# +
from __future__ import print_function
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import ipywidgets as widgets
import numpy as np
from math import sin, cos, pi, atan2
from random import randint 
from pylab import *
import warnings
warnings.filterwarnings('ignore')

def transafin(M,t,x):
    y=M@x+t
    return y

def sierpinsky():
    fig=plt.figure()
    ax=plt.gca()
    Tri=np.array([[0,0]])
    for i in range(8):
        tritrans=np.array([transafin([[0.5,0],[0,0.5]],[0,0],i) for i in Tri])
        tritrans2=np.array([transafin([[0.5,0],[0,0.5]],[0,0.5],i) for i in Tri])
        tritrans3=np.array([transafin([[0.5,0],[0,0.5]],[0.5,0],i) for i in Tri])
        Tri=np.concatenate((tritrans,tritrans2,tritrans3))
    plt.scatter(Tri.transpose()[0],Tri.transpose()[1],color='black',s=0.2)
    ax.set_xticks(np.arange(-0.2,1.4,0.2))
    ax.set_yticks(np.arange(-0.2,1.4,0.2))
    plt.grid()
    ax.axis("equal")
    
def fern():
    # initializing the list 
    x = [] 
    y = [] 

    # setting first element to 0 
    x.append(0) 
    y.append(0) 

    current = 0

    for i in range(1, 50000): 

        # generates a random integer between 1 and 100 
        z = randint(1, 100) 

        # the x and y coordinates of the equations 
        # are appended in the lists respectively. 

        # for the probability 0.01 
        if z == 1: 
            x.append(0) 
            y.append(0.16*(y[current])) 

        # for the probability 0.85     
        if z>= 2 and z<= 86: 
            x.append(0.85*(x[current]) + 0.04*(y[current])) 
            y.append(-0.04*(x[current]) + 0.85*(y[current])+1.6) 

        # for the probability 0.07     
        if z>= 87 and z<= 93: 
            x.append(0.2*(x[current]) - 0.26*(y[current])) 
            y.append(0.23*(x[current]) + 0.22*(y[current])+1.6) 

        # for the probability 0.07     
        if z>= 94 and z<= 100: 
            x.append(-0.15*(x[current]) + 0.28*(y[current])) 
            y.append(0.26*(x[current]) + 0.24*(y[current])+0.44) 

        current = current + 1

    plt.scatter(x, y, s = 0.2, edgecolor ='green') 
    plt.axis("equal")
    plt.show() 
    
def copoVonKoch(lado, n):
    x_vertice1 = 0
    y_vertice1 = 0

    x_vertice2 = lado * cos(2 * pi / 3)
    y_vertice2 = lado * sin(2 * pi / 3)

    x_vertice3 = lado * cos(pi / 3)
    y_vertice3 = lado * sin(pi / 3)

    curvaVonKoch(x_vertice1, y_vertice1, x_vertice2, y_vertice2, n)
    curvaVonKoch(x_vertice2, y_vertice2, x_vertice3, y_vertice3, n)
    curvaVonKoch(x_vertice3, y_vertice3, x_vertice1, y_vertice1, n)


def curvaVonKoch(xi, yi, xf, yf, n):
    if n == 0:
        plot([xi, xf], [yi, yf], lw=1.0, color='b')
    elif n > 0:
        x1 = xi + (xf - xi) / 3.0
        y1 = yi + (yf - yi) / 3.0

        x3 = xf - (xf - xi) / 3.0
        y3 = yf - (yf - yi) / 3.0

        radio = hypot(x3 - x1, y3 - y1)
        alpha = atan2((y3 - y1), (x3 - x1))
        alpha += pi / 3.0
        x2 = x1 + radio * cos(alpha)
        y2 = y1 + radio * sin(alpha)

        curvaVonKoch(xi, yi, x1, y1, n - 1)
        curvaVonKoch(x1, y1, x2, y2, n - 1)
        curvaVonKoch(x2, y2, x3, y3, n - 1)
        curvaVonKoch(x3, y3, xf, yf, n - 1)


def koch(lado, n):
    axes().set_xlim(0, lado)
    axes().set_ylim(-2, lado / 2.0)
    axes().set_aspect(1.0)
    title('Curva De Von Koch')
    xlim(0, lado)
    curvaVonKoch(0, 0, lado, 0, n)
    show()
    axes().set_xlim(-lado, lado)
    axes().set_ylim(-2, lado + 0.5 * lado)
    axes().set_aspect(1.0)
    title('Copo De Nieve De Koch')
    xlim(-lado, lado)
    copoVonKoch(lado, n)
    show()


def spski_carpet(ax, p, n, size):
    if n > 0:
        ax.add_patch(Rectangle((p[0, 0] - size / 6,
                                p[1, 0] - size / 6),
                               size / 3, size / 3,
                               facecolor=(0.5, 0.5, 0.5),
                               linewidth=0))
        q = np.array([[-size / 3], [-size / 3]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[-size / 3], [0]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[-size / 3], [size / 3]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[0], [-size / 3]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[0], [size / 3]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[size / 3], [-size / 3]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[size / 3], [0]])
        spski_carpet(ax, p + q, n - 1, size / 3)
        q = np.array([[size / 3], [size / 3]])
        spski_carpet(ax, p + q, n - 1, size / 3)

def sierpinski_carpet():
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = plt.gca()
    p = np.array([[0], [0]])
    spski_carpet(ax, p, 4, 1)
    ax.add_patch(Rectangle((-1 / 2, -1 / 2), 1, 1,
                           fill=False , edgecolor=(0, 0, 0),
                           linewidth=0.5))
    plt.axis('equal')
    plt.axis('off')
    plt.show()
