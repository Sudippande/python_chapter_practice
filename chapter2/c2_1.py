a=int(input("Enter first number: "))
b=int(input ("Enter the number that will divide the other number: "))

ty=type(a) #here i have found a type
print(ty)
print("The remainder is :",a%b)
if a>b:
    print(a,"is Grater than ",b)
else:
    print(b,"is grater than",a)
