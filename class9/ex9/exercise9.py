#!/usr/bin/env python
"""
    Excercise 9: Write a Python script
"""
from sys import path
path.append("/home/befthimiou/be_pynet_course/class9")
from pprint import pprint
import mytest
import os

if __name__ == '__main__':
    print 'Corrent working Directory:'
    print '-' * 30
    cwd = os.getcwd()
    print cwd
    print
    print 'Python sys path:'
    pprint (path)
    print '-' * 50
    print
    
    print 'func1'
    print '-' *15
    mytest.func1()
    print
    print 'func2'
    print '-' *15
    mytest.func2()
    print
    print 'func3'
    print '-' *15
    mytest.func3()

    a_class = mytest.MyClass(10, 25, 30)
    print
    print 'hello'
    print '-' *15
    a_class.hello()
    print
    print 'not hello'
    print '-' *15
    a_class.not_hello()
