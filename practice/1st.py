# # a,b,c,d=1,2,3,4
# # print(a)
# # print(b)
# # print(c,end="")
# # print(d,end=)

# # a= 3.14+5j
# # b=4-3j
# # print(a+b)

# import fraction
# n=fraction(5,3)
# print(n.numerator)

# a=[1,2,3,4,5]
# a=tuple(()
# from collections import namedtuple
# Vision=namedtuple('Vision',['left','right'])
# vision=Vision(3.56,2.78)
# print(vision[0])
# print(vision.left)
# print(vision.right)

# from enum import Enum
# def tl(Enum):
#     RED=1
#     GREEN=2
#     YELLOW=3

# print(tl.RED.value)
# print(tl.GREEN.name)
# name=["sudip",'ram','hari']
# for position in range(len(name)):
#     print(position,name[position])

# a=[1,2,3,4]
# b=a.copy()
# print(a==b,a is b)

class Meta(type):
    pass
class A(metaclass=Meta):
    pass
print(type(A))