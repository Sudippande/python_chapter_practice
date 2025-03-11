# *
# **
# ***
# for i in range(3):
#     for j in range(i+1):
#         print("*",end='')
#     print()

# ****
# ***
# **
# *

# for i in range(5):
#     print("*"*(5-i),end="")
#     print("")

#    ***
#     **
#      *

# for i in range(5):
#     print(" "*i,end="")
#     print("*"*(5-i))

#     *
#    **
#   ***

# for i in range(4):
#     print(" "*(4-i),end='')
#     print("*"*i)

        #    *
        #   * *
        #  * * *
        # * * * *
# for i in range(5):
#     print(" "*(5-i),end="")
#     print(" * "*i,end="")
#     print(" "*(5-i))
#     print()


# * * * *
#  * * *
#   * *
#    *

# for i in range (5):
#     print(" "*i,end="")
#     print(" * "*(5-i),end="")
#     print(" "*i,end="")
#     print()

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

""" This code will give and interesting pattern."""
# for j in range(1,8,2):
#     for i in range(3):
#         print(" "*(3-i),end="")
#         print("*"*j,end="")
#         print(" "*(3-i),end="")
#         print()

"""For above mentioned code"""
n = 4  # Number of rows in the top half

# Top half of the pattern
# for i in range(n):
#     spaces = n - i - 1
#     stars = 2 * i + 1
#     print(" " * spaces + "*" * stars)

# Bottom half of the pattern
# for i in range(n - 2, -1, -1):
#     spaces = n - i - 1
#     stars = 2 * i + 1
#     print(" " * spaces + "*" * stars)

for i in range(n - 2, -1, -1):
    
    print(i)
