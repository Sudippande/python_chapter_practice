# x=lambda x,y: f"{x} is grater" if x>y else f"{y} is grater"
# res=x(5,2)
# print(res)


# Prime number
# n=12
# m=100
# for i in range(2,m+1):
#     if i>1:
#         for j in range(2,int(i**0.5)+1):
#             if(i%j ==0):
#                 break
#         else:
#             print(i)


# t=input("Enter text:")
# w=t.split()
# f={}
# for i in w:
#     f[i]=f.get(i,0)+1
# print("Word Frequency:")
# for i ,count in f.items():
#     print(f"{i}:{count}")
def print_hollow_square(n):
    for i in range(n):
        for j in range( n):
            if i ==0 or i ==n-1 or j ==0 or j ==n-1:
                print("*",end="")
            else:
                print(" ",end=" ")
        print()
print_hollow_square(5)