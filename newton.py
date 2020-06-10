# -*- coding: utf-8 -*-
# +
from __future__ import print_function
import matplotlib as plt
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import sympy as spp
from sympy.parsing.sympy_parser import parse_expr
import ipywidgets as widgets
import numpy as N
from PIL import Image

#Número de iteraciones para buscar una raíz.
maxit = 32
#Valor aproximado a cero para calcular la derivada aproximada.
h = 1e-6
#Valor de tolerancia para determinar que se encontró una solución.
eps = 1e-3

#Función que calcula la distancia de un elemento z que
#pertenece a los complejos en un conjunto de números complejos
#elige la mínima distancia y devuelvel el elemento de la 
#lista al que más se acerca, así como la distancia.
def distPC(Z,z):
    d0=100
    item=0
    for i in range(len(Z)):
        d=abs(Z[i]-z)
        if d<d0:
            d0=d
            item=i
        else:
            None
    return d0,item

#Función que recibe una función fn y usa el método de Newton
#para dibujar un fractal. Cada raíz se representa con un color
#y los tonos de ese color identifican la velocidad de conver-
#gencia a una raíz.
def fractal(fn, imgx=800, imgy=800, xa=-1, xb=1, ya=-1, yb=1):
    image=Image.new("RGBA",(imgx,imgy))
    f = eval('lambda z: ' + fn)
    Z=[]
    maxd=0.005
    for y in range(imgy):
        zy=y*(yb-ya)/(imgy-1)+ya
        for x in range(imgx):
            zx=x*(xb-xa)/(imgx-1)+xa
            z=complex(zx,zy)
            for i in range(maxit):
                dz=(f(z+complex(h,h))-f(z))/complex(h,h)
                z0=z-f(z)/dz
                if abs(z0-z)<eps:
                    break
                z=z0
            #Se obtuvo una raiz o se superó el número de iteraciones
            if i < (maxit-1):
                dist = distPC(Z,z)
                if dist[0]<maxd:
                    item = dist[1]
                else:
                    Z.append(z)
                    item = len(Z)-1
                r=((item+7)%len(Z)*32)%225
                g=((item+5)%len(Z)*57)%225
                b=((item)%len(Z)*26)%225
                a= 64 + int(i*192/maxit)
            else:
                #El punto non converge a ninguna raíz, se pone el pixel en Blanco.
                r = 255
                g = 255
                b = 255
                a = 255
                                    
            image.putpixel((x,y),(r,g,b,a))

    wf = widgets.HTMLMath(
        value="$f(z)={}$ <p> Raices:{}".format( \
               spp.latex(parse_expr(fn)),Z),
        placeholder='',
        description='',
        layout=Layout(width='100%'),
    )
    display(wf)
            
    return image

#Función interactiva.
def custom_fractal():
    interact_manual(fractal, fn="z**3-1")


# -


