# a, b = 100, 200, 300
# ValueError: too many values to unpack (expected 2)

# a, b, c = 100, 200
# ValueError: not enough values to unpack (expected 3, got 2)

a, *b = 100, 200, 300

print(a)
print(type(a))
# 100
# <class 'int'>

print(b)
print(type(b))
# [200, 300]
# <class 'list'>

*a, b = 100, 200, 300

print(a)
print(type(a))
# [100, 200]
# <class 'list'>

print(b)
print(type(b))
# 300
# <class 'int'>

a, b, c = 0.1, 100, 'string'

print(a)
# 0.1

print(b)
# 100

print(c)
# string