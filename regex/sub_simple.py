# coding=utf-8

import re

t = re.sub('\d+', '_bingo_', 'haha123hehe456hiahia')
print(t)
t = re.sub('\d+', '_bingo_', 'haha123hehe456hiahia', 1)
print(t)
t = re.subn('\d+', '_bingo_', 'haha123hehe456hiahia')
print(t)
