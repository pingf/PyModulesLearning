# coding=utf-8

a1 = [0, 1, 2]
a2 = iter(a1)
b1 = {'a': 0, 'b': 1, 'c': 2}
b2 = iter(b1)
c1 = (0, 1, 2)
c2 = iter(c1)
d1 = range(3)
d2 = iter(d1)

print(type(a1))
print(type(a2))
print(type(b1))
print(type(b2))
print(type(c1))
print(type(c2))
print(type(d1))
print(type(d2))

e1 = enumerate(a1)
print(type(e1))
for i, v in e1:
    print(i, v)

f1 = (x for x in a1)
print(type(f1))
for v in f1:
    print(v)
