# coding=utf-8

import re

t = re.search('\d{3}', 'abcd 1234 efg')
print(t)
print(t.span())
print(t.group())
t = re.search('(\d{3})', 'abcd 1234 efg')
print(t.groups())
t = re.search('(\d{3}) (\w+)', 'abcd 1234 efg')
print(t.groups())
t = re.search('(?P<gp1>\d{3}) (?P<gp2>\w+)', 'abcd 1234 efg')
print(t.group())
print(type(t.group()))
print(t.groups())
print(t.group('gp2'))
print(t.groupdict()['gp1'])
print(t.groupdict())
#要说的是?P<>中指定的是name， ?P=后则是引用，必须和最早的严格一致
t = re.search('(?P<three>\d{3}) \w+ (?P=three)', '123 abcdefg 456')
print(t)
t = re.search('(?P<three>\d{3}) \w+ (?P=three)', '123 abcdefg 123')
print(t.group('three'))
