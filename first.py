"""
*
**
***
****
"""
# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print("")
'''
# ****
# ***
# **
# *

for i in range(1,5):
    for j in range(5-i):
        print("*",end="")
    print("")
    
    or

for i in range (1,6):
 print("*"*(6-i))
 
 
 
 
 
 
 
 3rd pattern
 
*****
 ****
  ***
   **
    *  

for i in range (1,6):
 print("*"*(6-i))
 print(" "*i,end="")

print("")
    
 
 
 
#  4th pattern 
 
      
# *

# ****

# *********

# ****************

# *************************

# for i in range(1,6):
#     print(" "*(6-i))
#     for j in range(i):
#         print("*"*i,end="")
#     print("")





# 5 pattern 

# ***
# * *
# ***

#  '''
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#          print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")
#     '''
# ***
#  *    
# ***


# '''
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         m=n/3
#         o=int(m)
#         print(" *"*o,end="")
#     print("")
