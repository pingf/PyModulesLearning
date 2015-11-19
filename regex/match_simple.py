# coding=utf-8

import re

t = re.match('\d{3}', 'abcd 1234 efg')
print(t)
t = re.fullmatch('\d{3}', '123')
print(t)
t = re.match('\d{3}', '1234 efg')
print(t)
print(t.span())
print(t.group())
t = re.match('\d{3}', '1234 efg')
print(t)
print(t.span())
print(t.group())
