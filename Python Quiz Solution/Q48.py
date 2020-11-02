import numpy
from pandas.core.arrays.sparse import dtype


a = numpy.arange(100000,dtype=int)
print(a.size*4)