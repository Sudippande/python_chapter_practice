# n=int(input("Enter The Number to find the multiplication:"))
# mul=0
# for i in range(1,11):
#     mul=n*i
#     print(f"{i}*{n}=",mul)

# l=["sudip","ram","sujita","Hari"]
# for i in l:
#     if(i.startswith("s")):
#         print(f"Namaste {i}")
#     else:
#         print(i)
        
    
    #WAp to find  a entered number is prime or not
# #sum  of first n natural numbers
# m=int(input("Enter n natural number: "))
# i=1
# sum=0
# while(i<=m):
#    sum=sum+i
#    i+=1

# print(sum)


''' Factorial calculation'''
# f=int(input("Enter number:"))
# fact=1
# for i in range(1,f+1):
#     fact=fact*i
# print(f"Factorial of number {f} is:",fact)

"""star pattern"""
n=int(input("Enter number:"))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"*(i+1-1),end="")
  print("\n")

# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     for j in range(i+1-1):
#         print("*",end="")
#     print("")



# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n,end="")
#     else:   
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")
        
n=int(input("Enter number:"))
mun=11
for i in range(1,11):
    mun-=1
    print(f"Multiplication on {n} * {mun} is :",mun*n)