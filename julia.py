# -*- coding: utf-8 -*-
# +
from __future__ import print_function
import matplotlib as plt
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import ipywidgets as widgets
import numpy as N

from PIL import Image

maxit = 32
h = 1e-6
eps = 1e-3

def fractal(fn, imgx=800, imgy=800, xa=-2, xb=2, ya=-2, yb=2):
    image=Image.new("RGBA",(imgx,imgy))
    f = eval('lambda z: ' + fn)

    for y in range (imgy):
        zy=y*(yb-ya)/(imgy-1)+ya
        for x in range (imgx):
            zx=x*(xb-xa)/(imgx-1)+xa
            z=complex(zx,zy)
            for i in range (maxit):
                z0=f(z)
                if abs(z)>1000:
                    break
                z=z0
                r=i*8
                g=i*8
                b=i*8
                image.putpixel((x,y),(r,g,b))    
    return image

def custom_fractal():
    interact_manual(fractal, fn="z**2")


# -


