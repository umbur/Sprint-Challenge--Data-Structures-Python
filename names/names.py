import time

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

# New solution to reduce runtime:
# Defineing storage which is an object and will act as a cache
storage = {}
# Defining duplicates array which should store the duplicated values
duplicates = []

# Looping through the values of names_1
for name_1 in names_1:
    # Assigning values of names_1 to the storage object
    storage[name_1] = name_1
# Looping through the values of names_2
for name_2 in names_2:
# If the values in storage equals values in names_2
        if name_1 in storage == name_2:
# Then append those values to the duplicates array
            duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

