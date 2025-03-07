# def fibo(n):
#     a,b=0,1
#     while(a<n):
#         a,b=b,a+b
#         print(a,end=' ')
    

# fibo(6)

#program to arggs
# i=5
# def f(arg):
#     print(arg)
# i=7
# i=8
# f(i)

# def f(a,L=[]):
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))

# pairs=[(1,'one'),(2,'two'),(3,'THREE'),(4,'four')]
# pairs.sort(key=lambda pair:pair[1].lower())
# print(pairs)

# n=5
# result=[(x,y,z) for x in range(3) for y in range(3) for z in range(3) if x+y+z !=n]
# print(result)

# matrix=[[1,2,3],[3,4,5],[2,3,5],[7,8,9,0],]
# result=[[row[i] for row in matrix] for i in range(3)]
# print(result)

def d_t():
    def noo():
        spam="local"
    def non():
        nonlocal spam
        spam="none local"
    def glb():
        global spam
        spam="It is for global"
    spam="test spam"
    def noo()
    print("this one is 1st one",spam)
    def non()
    print("This is a local scope",spam)
    def glb()
    print("this is for a global ",spam)
def d_t()
print("In global scope",spam)
