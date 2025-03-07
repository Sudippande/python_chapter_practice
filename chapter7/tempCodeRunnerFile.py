n=int(input("Enter number:"))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"*(i+1-1),end="")
  print("\n")