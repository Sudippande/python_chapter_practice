# class Myclass:
#     i=123
#     def f(self):
#         return 'hello world !'
# # x=Myclass()
# # print(x.i)
# # print(x.f())
# print(Myclass.i)


class complex:
    def __init__(self,first,last):
        self.r=first
        self.s=last
    def display(self):
        return self.r,self.s
y=complex(12,34)
print(y.r," ",y.s)
print("After this !")
res=y.display()
print(res)