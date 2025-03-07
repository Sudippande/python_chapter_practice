# info={"name":"Sudip",
#              "Age":34,
#              "Address":"Nepal",
#              "list":[1,2,3],
#              "tuple":(11,22,33)}
# print(information["name"])
# print(info.items())
# print(info.keys())
# print(info.values())

# to update dictionary we can use this function
# info.update({"name":"Sudip pande","fname":"Sujita"})
# print(info)

# print(info)

# multiplication_table = {x: {y: x * y for y in range(1, 6)} for x in range(1, 4)}
# print(multiplication_table)
# Output:
# {
#   1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
#   2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
#   3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}
# }

mul={x:{y: x*y for y in range(1,11)} for x in range(1,11)}
print(mul)