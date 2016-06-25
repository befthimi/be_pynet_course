#!/usr/bin/env python
"""
my world module
"""

def func1():
    """
    func1 function
    """
    print 'executing the world function func1'

class MyClass(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        sum = self.x + self.y + self.z
        print 'Hello. Sum of input is: %d' %sum

    def not_hello(self):
        prod = self.x * self.y * self.z
        print 'Not Hello, prints product: %d' %prod

class MyChildClass(MyClass):
    """
    overide hello Method of parent MyClass.
    """

    def hello(self):
        average_val = (self.x + self.y + self.z)/3
        print 'Hello overide. The average value is: %d' %average_val

if __name__ == '__main__':
    print 'main of world module'
