# -*- coding: utf-8 -*-
# +
from __future__ import print_function
import matplotlib as plt
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import ipywidgets as widgets
import numpy as N
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

#Número de iteraciones
maxit = 32

#Función que gráfica un fractal de Mandelbrot a partir
#de una función fn.
def fractal(fn, imgx=800, imgy=800, xa=-2, xb=2, ya=-2, yb=2):
    image=Image.new("RGBA",(imgx,imgy))
    f = eval('lambda z,a,b: ' + fn)

    for y in range (imgy):
        zy=y*(yb-ya)/(imgy-1)+ya
        for x in range (imgx):
            zx=x*(xb-xa)/(imgx-1)+xa
            z=0
            for i in range (maxit):
                z0=f(z,zx ,zy )
                if abs(z)>1000:
                    break
                z=z0
                r=i*12
                g=i*10
                b=i*7
                image.putpixel((x,y),(r,g,b))
            
    return image

#Función interactiva.
def custom_fractal():
    interact_manual(fractal, fn="z**2+complex(a,b)")


# -


