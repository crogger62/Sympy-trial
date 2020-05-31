# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:21:31 2020

@author: craig

Docs are here: https://docs.sympy.org/latest/tutorial/intro.html

Status 5/31/20:
* no errors thrown with sympy
* no output; Latex would be an option but not sure how to coax it out
* using sympy with reticulate() in R not working

"""
import sympy
import math

from sympy import *
x = symbols('x')
a = Integral(cos(x)*exp(x), x)
Eq(a, a.doit())

math.sqrt(9)

#
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)
diff(sin(x) * exp(x),x)