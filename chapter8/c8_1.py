#recursion of factorail


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#          return n*factorial(n-1)
# a=int(input("Ënter one number to calculate factorial:"))
# b=factorial(a)
# print("Factorial  is ",b)

#Fibonacci
# def fibo(n):
#     if(n<=1):
#         return n
#     else:
#         return (fibo(n-1)+fibo(n-2))
    
# a=fibo(12)
# print("Fibo naci of f is :",a)

""" Recursive function to multiply 2 numbers"""
# def mul(a,b):
#     if(b==1):
#         return a
#     else:
#         return (a+mul(a,b-1))
# c=mul(3,6)
# print(c)

''' Tower of  Hanoe probalem'''
# def toh(n,char_from,char_to,char_in):
#     if(n==1):
#         print("Take disk 1 from peg",char_from,"to peg",char_to)
#         return
#     toh(n-1,char_from,char_in,char_to)
#     print("Take disk",n,"from peg",char_from,"to peg",char_to)
#     toh(n-1,char_in,char_to,char_from)
# toh(5,"A","C","B")

#GCD Calculation
# def hcf(n,m):
#     if(m==0):
#         return n
#     else:
#         return hcf(m,n%m)
# n=int(input("Enter one number:"))
# m=int(input("Enter one number:"))
# o=hcf(n,m)
# print(o)

