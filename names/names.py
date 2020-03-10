import time
from BinarySearchTree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# The default solution which takes longer time to execute 
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# print(duplicates)

# New solution to reduce runtime:
# Defining duplicates array which should store the duplicated values
# The python sets solution:
duplicates = []
name2 = set(names_2)
for value in names_1:
    if value in name2:
        duplicates.append(value)
# print(duplicates)
# bst = BinarySearchTree(names_1[0])
# for i in range(1, len(names_1)-1):
# #     print(len(names_1))
#     bst.insert(names_1[i])

# for name in names_2:
#     if (bst.contains(name)):
#         duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

