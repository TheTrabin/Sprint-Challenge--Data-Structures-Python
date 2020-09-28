import time
from binary_search_tree import BSTNode

# First I had to properly import the file, taken liberty from viewing filesio.py from out first run with Python - Intro-Python-I
# The python file couldn't initially find the text files, even though they were self contained. Seems Python favors Root over others.
# 35 seconds?!?!?! I actually quit it the first time I ran it because I thought something was BROKEN!!!
# Alright,, first thing's first, we comment out the old code, and look into how to change that from O(n^3) to something more linear.
# Build a Node, like the Double linked list, because we're comparing two lists.
# Then we set it up to view doubles, and append the name to the array and print it out.
# imported BSTNode from Data-Structures repository, applied to use it, and came up with 0.8 seconds!!!! Avg time: Under 1sec

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

namesearch = BSTNode(names_1[0])

for names1 in names_1:
    namesearch.insert(names1)
for names2 in names_2:
    if namesearch.contains(names2):
        duplicates.append(names2)


# built in comparison, exact names, 10 seconds longer than the above using BSTNode.
# dup = [val for val in names_1 if val in names_2] 

# print(dup)

# 0.8 seconds.
# def intersect(names_1, names_2):
#     return list(set(names_1) & set(names_2))

# print(intersect(names_1, names_2))


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.



