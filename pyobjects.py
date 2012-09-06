#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import string

if sys.argv.__len__() < 2:
    print 'Usage: %s </usr/lib/python2.7/module.py>' % sys.argv.__getitem__(0)
    exit(1)
pyFile = sys.argv.__getitem__(1)
module_name = os.path.basename(pyFile).replace('.py', '')
fd = open(pyFile, 'r')
lines = fd.readlines()
fd.close()
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_
symbols = string.letters.__add__('_')

#variable = value
def doesVariable(line):
    if (
        line.__getitem__(0) in symbols
        and
        line.__contains__(' = ')
        and
        #' ' not in line.__getslice__(0, line.index(' = ')).strip()
        not line.__getslice__(0, line.index(' = ')).strip().__contains__(' ')
       ):
       variable_name = line.partition(' = ').__getitem__(0).rstrip()
       print module_name + '.' + variable_name

#class SomeClass(BaseClass):
#012345
def doesClass(line):
    if (
        line.__getslice__(0, 6) == 'class '
        and
        (
         line.__contains__(':')
         or
         line.__contains__('(')
        )
       ):
       class_name = line.__getslice__(6, line.__len__())
       class_name = class_name.rpartition(':').__getitem__(0).strip()
       print module_name + '.' + class_name
       #class SomeClass: pass
       doesclass = class_name.partition('(').__getitem__(0).strip()
       tryDoc(doesclass)
       #We need to check the methods.
       int = lines.index(line).__add__(1)
       to = lines.__len__().__sub__(1)
       #print int, to
       nextline = lines.__getitem__(int)
       while (
              nextline.__getitem__(0) not in symbols
              and
              int < to
             ):
           doesDef(nextline.strip(), doesclass=doesclass, tabs='    ', index=int)
           int += 1
           nextline = lines.__getitem__(int)
           #print repr(nextline)
           #print int

#def function():
#0123
def doesDef(line, doesclass='', tabs='', index=None):
    if (
        line.__getslice__(0, 4) == 'def '
        and
        (
         line.__contains__(':')
         or
         line.__contains__('(')
        )
       ):
       def_name = line.__getslice__(4, line.__len__()).strip()
       #lines is global. :)
       while (
              ':' not in def_name
             ):
           #Nice hack found luckily.
           if not index:
               index = lines.index(line).__add__(1)
           elif index:
               index = index.__add__(1)
           subline = lines[index]
           def_name += ' ' + subline.strip()
           #print index
           #Left after founded hack.
           #index += 1
       def_name = def_name.rpartition(':').__getitem__(0).strip()
       if doesclass:
           print tabs + module_name + '.' + doesclass + '.' + def_name
       else:
           print tabs + module_name + '.' + def_name
       def_name = def_name.partition('(').__getitem__(0).strip()
       tryDoc(def_name, doesclass=doesclass)

def tryDoc(object_name, doesclass=None):
    try:
        import __builtin__
        #Magic.
        module = __builtin__.__import__(module_name)

        #You suppose `module.__getattribute__(object_name)' works?! Ain't it. :D
        if doesclass:
            classobject = module.__getattribute__(doesclass)
            object = getattr(classobject, object_name)
        else:
            object = module.__getattribute__(object_name)
        #object.__doc__
        docstring = getattr(object, '__doc__')
        #Exists?
        if docstring:
            print docstring
    except:
        pass

for line in lines:
    doesVariable(line)
for line in lines:
    doesClass(line)
for line in lines:
    doesDef(line)
