# a=[]
# for i in range(1,7):
#     mark=int(input(f"enter the marks of student{i}: "))
#     a.append(mark)
# a.sort()
# print("sorted:", a)

#addition of list
''' 
b=[]
for i in range(4):
    a=int(input(f"Enter the name {i}: "))
    b.append(a)
print(b)

sum=0
for j in b:
    
    sum=sum+j
    
print("Sum is :",sum)

   '''

'''
a=[]
b=[]
b1=int(input("enter numbers:"))
a.append(b1)
b2=int(input("enter numbers:"))
a.append(b2)
b3=int(input("enter numbers:"))
a.append(b3)
b4=int(input("enter numbers:"))
a.append(b4)
b.append(b1+b2+b3+b4)
print(a)
print("usum is :",b)
'''

# items=[1,7,3,0,4,9]
# even=filter(lambda x: x%2==0,items)
# print(list(even))

#file Creation in python

# with open("sudip.txt","w") as f:
#     print(f.write("Hello World !"))
#     print("File Created successfully !")


#file opening in python
# with open("sudip.txt","r") as f:
#     print(f.read())

#use of Zip
# name=['sudip','ram']
# age=[22,24]
# print(list(zip(name,age)))

#use case of all and any method
print(all([True,False,False])) # return true id all elements are tru and any returns true if any element are truthy
# print(isinstance(123.,float))
# len=123.12
# print(help(len))

# a=7
# b=0
# c=9
# temp=a
# print("print it before swap",a,b,c)
# a=temp
# a=c
# b=b
# c=temp
# print("after swapping",a,b,c)

#WAP to count number of 0 in tuple
a=(1,2,3,0,0,0,4)
print(a.count(0))