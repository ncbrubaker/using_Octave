import oct2py
from oct2py import octave
oc = oct2py.Oct2Py()
x = oc.zeros(3,3)
print(x, x.dtype)