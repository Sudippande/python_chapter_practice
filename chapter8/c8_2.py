# def great(a,b,c):
#     print(max(a,b,c))
# great("apple","grapes","ant")

#WAP to convert celsius  to fahrenheit
# def cel_fah(c):
#     f=(9/5)*c+32
#     return f
# t=cel_fah(37)
# print(t)

#Write a recursive function to sum first n natural number
# def sum(n):
#     if(n==0):
#         return 0
#     else:
#         a=n+sum(n-1)
#         return a
# recursive_result=sum(5)
# print("Recursive sum  is:",recursive_result)

"""
***
**
*

"""
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)
        
        
# pattern(3)


# WA python program to converts inches into cms
# formula = cm= inches*2.54
# def in_cm(inches):
#  return inches*2.54
# a=in_cm(5)
# print(a)


# write a python function to remove a given word from a list ad strip it at the same time.
def li_st(a,w):
    a=[]
    for i in a:
        if not (i==w):
            a.append(i.strip(w))
            
    return a
    
            

   
   
a=[1,2,3,4,"sudip","sujita"]
print(li_st(a,"su"))