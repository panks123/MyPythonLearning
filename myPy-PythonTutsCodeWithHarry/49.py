# Generators


# Iterable--- object in which __iter__() or__getitem__() are defined --- when we run these methods on that
            # object then it will return an iterator   e.g. lists,strings,tuples etc.

# Iterator---object in which __next__() is defined
# Iteration---process


# generator ---those objects which can be traversed only once

# e.g.

for i in range(5):   # here range is a generator ,it has generated the values on the fly
    print(i)


# creating a generator

def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)


g=gen(7)
"""
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
#print(g.__next__())
"""

print("xxx")
for i in g:
    print(i)

h="Harry"

it=iter(h)
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())