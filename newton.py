# +
from __future__ import print_function
import matplotlib as plt
from ipywidgets import interact, interactive, fixed, interact_manual, Layout
import ipywidgets as widgets

from PIL import Image

maxit = 32
h = 1e-6
eps = 1e-3

def fractal(fn, imgx=800, imgy=800, xa=-1, xb=1, ya=-1, yb=1):
    image=Image.new("RGB",(imgx,imgy))
    f = eval('lambda z: ' + fn)
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
                r=i%4*64
                g=i%8*32
                b=i%16*16
                image.putpixel((x,y),(r,g,b))
    return image

interact_manual(fractal, fn="z**3-1")


