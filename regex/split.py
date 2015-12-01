# coding=utf-8

import re

t = re.split('\s+', 'aaa bbb 111 222')
print(t)
t = re.split('\s+', 'aaa bbb 111 222', 1)
print(t)
