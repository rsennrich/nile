"""
Vector class

Implementation of sparse vectors as Python dictionary.
In addition to normal dictionary operations, offers the following methods:

a = Vector({'a':1, 'b':2}) # initialisation like dictionary
b = a.copy() # shallow copy
b['c'] # unknown key returns 0, but is not added to dictionary
b['c'] = 3 # assignment like dictionary

a + b # vector addition
a - b # vector subtraction
a * 2 # scalar product
a / 2 # scalar division
a.dot(b) # dot product

#in-place operations:

a += b # vector addition
a -= b # vector subtraction
a *= 2 # scalar product
a /= 2 # scalar division

"""

from __future__ import division

class Vector(dict):

    def __add__(self, other):
        """vector addition"""
        if not isinstance(other, dict):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        new = self.copy()
        for key,value in other.items():
            new[key] += value
        return new

    def __iadd__(self, other):
        """vector addition (in-place)"""
        if not isinstance(other, dict):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        for key,value in other.items():
            self[key] += value
        return self

    def __sub__(self, other):
        """vector subtraction"""
        if not isinstance(other, dict):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        new = self.copy()
        for key,value in other.items():
            new[key] -= value
        return new

    def __isub__(self, other):
        """vector subtraction (in-place)"""
        if not isinstance(other, dict):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        for key,value in other.items():
            self[key] -= value
        return self

    def __mul__(self, other):
        """scalar product"""
        if not isinstance(other, (int, float)):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        new = self.copy()
        for key in new:
            new[key] *= other
        return new

    def __imul__(self, other):
        """scalar product (in-place)"""
        if not isinstance(other, (int, float)):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        for key in self:
            self[key] *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)


    def __div__(self, other):
        """scalar division"""
        if not isinstance(other, (int, float)):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        new = self.copy()
        for key in new:
            new[key] /= other
        return new

    def __idiv__(self, other):
        """scalar division (in-place)"""
        if not isinstance(other, (int, float)):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        for key in self:
            self[key] /= other
        return self

    def __missing__(self, key):
        return 0

    def copy(self):
        return Vector(self)

    def dot(self, other):
        """dot product"""
        if not isinstance(other, dict):
            raise TypeError("unsupported operand type(s) for: '"+str(self.__class__)+"' and '"+str(other.__class__)+"'")
        s = 0
        for key,value in self.items():
            s += value * other[key]
        return s