#coding=utf-8

t = re.sub('(?P<three>\d{3})','\g<three>iii', '123 abcdefg 456')
print(t)