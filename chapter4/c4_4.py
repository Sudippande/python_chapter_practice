#write a program to display the marks of 6 students and display them in a sorted manner.
a=[]
a1=int(input("Enter marks of 1st student: "))
a.append(a1)
a2=int(input("Enter marks of 2st student: "))
a.append(a2)
a3=int(input("Enter marks of 3st student: "))
a.append(a3)
a4=int(input("Enter marks of 4st student: "))
a.append(a4)
a5=int(input("Enter marks of 5st student: "))
a.append(a5)
a6=int(input("Enter marks of 6st student: "))
a.append(a6) 

a.sort()
print(a)
