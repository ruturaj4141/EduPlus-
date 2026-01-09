# Set Basics and Modification
# Create a set containing five different country names and print it.
# Create a set with duplicate numbers and print it to see how duplicates are handled.
# Use the set() constructor to create a set from a list of fruits.
# Add a new element into an existing set using the add() method.
# Add multiple elements into a set using the update() method.
# Try adding a duplicate element to the set and check if it changes.
# Remove an element from a set using the remove() method.
# Remove an element safely using discard() without raising an error.
# Remove a random element using pop() and print both removed and remaining elements.
# Clear all elements from a set using clear() and print it.
# Mathematical Set Operations
# Create two sets of numbers and perform a union operation.
# Perform intersection between two sets to find common elements.
# Perform difference between two sets to find unique elements from the first set.
# Perform symmetric difference between two sets and print the result.
# Check if one set is a subset of another using the issubset() method.
# Check if one set is a superset of another using the issuperset() method.
# Check if two sets have no common elements using the isdisjoint() method.
# Membership and Built-in Functions
# Use the in keyword to check if a particular element exists in a set.
# Use the not in keyword to check if an element does not exist in a set.
# Find the total number of elements in a set using len().
# Find the maximum and minimum element from a numeric set using max() and min().
# Find the sum of all elements from a numeric set using sum().
# Convert a set into a sorted list in ascending order using sorted().
# Sort a set in descending order using sorted() with reverse=True.
# Use any() to check if at least one True value exists in a Boolean set.
# Use all() to check if all values in a Boolean set are True.
# Advanced Actions and Practical Exercises
# Copy a set using copy() and verify both sets are independent.
# Delete a set completely using the del keyword and observe the result.
# Convert a list with duplicate values into a set to remove duplicates.
# Create two sets of student names (from two different classes) and find:
# a) Common students (intersection)
# b) Students only in class A (difference)
# c) All unique students (union)

# Create a set containing five different country names and print it.
country={"india","america","china","nepal","vakanda"}
print(country)

# Create a set with duplicate numbers and print it to see how duplicates are handled.
duplicate_numbers={1,2,3,4,2,3,6,7,5,}
print(duplicate_numbers)

# Use the set() constructor to create a set from a list of fruits.
fruits=["apple","banana","chiku"]
print(set(fruits))

# Add a new element into an existing set using the add() method.
new_fruit={"apple","chiku","mango"}
new_fruit.add("jackfruit")
print(new_fruit)

# Add multiple elements into a set using the update() method.
new_fruit.update(["watermelon","cherry"])
print(new_fruit)

# Try adding a duplicate element to the set and check if it changes.
new_fruit.add("apple")
print(new_fruit)

# Remove an element from a set using the remove() method.
new_fruit.remove("apple")
print(new_fruit)

# Remove an element safely using discard() without raising an error.
new_fruit.discard("pineapple")
print(new_fruit)

# Remove a random element using pop() and print both removed and remaining elements.
popped_element=new_fruit.pop()
print("popped element:",popped_element)
print(new_fruit)

# Create two sets of numbers and perform a union operation.
a={1,2,3,4,5}
b={3,4,5,6,7,8,9}
print("union",a|b)

# Perform intersection between two sets to find common elements.
print("intersection",a&b)

# Perform difference between two sets to find unique elements from the first set.
print("unique elements from first set", a-b)

# Perform symmetric difference between two sets and print the result.
print("symmentric difference",a^b)

# Check if one set is a subset of another using the issubset() method.
print("is a subset of b?",a.issubset(b))

# Check if one set is a superset of another using the issuperset() method.
print("is a superset of b?",a.issuperset(b))

# Check if two sets have no common elements using the isdisjoint() method.
print("is a disjoint b?",a.isdisjoint(b))

# Use the in keyword to check if a particular element exists in a set.
print("is a in b?", a in b)

# Use the not in keyword to check if an element does not exist in a set.
print("is a not in b?", a not in b)

# Find the total number of elements in a set using len().
print("total number of elements are",len(a))

# Find the maximum and minimum element from a numeric set using max() and min().
print("maximum element:",max(a))
print("minimum element:",min(a))

# Find the sum of all elements from a numeric set using sum().
print("total sum of all elements",sum(a))

# Convert a set into a sorted list in ascending order using sorted().
print("sorted set of a",sorted(a))

# Sort a set in descending order using sorted() with reverse=True.
print("sorted set of a in descending order",sorted(a, reverse=True))

# Use any() to check if at least one True value exists in a Boolean set.
boolean_set={1,0,1,0}
print("if at least one True value exists in a Boolean set true or false?",any(boolean_set))

# Use all() to check if all values in a Boolean set are True.
print("if all values in a Boolean set are True or false?",all(boolean_set))

# Copy a set using copy() and verify both sets are independent.
copieda=a.copy()
print(copieda)
copieda.add(25)
print(copieda)
print(a)

# Convert a list with duplicate values into a set to remove duplicates.
my_list=[1,2,3,3,4,5,5,1]
new_set=set(my_list)
print("converted list into set with no duplicates",new_set)

# Create two sets of student names (from two different classes) and find:
# a) Common students (intersection)
# b) Students only in class A (difference)
# c) All unique students (union)
classa={"a","e","i","b"}
classb={"a","b","c","d","e"}
print("common students",a&b)
print(" students only in a",a-b)
print("all unique students",a|b)

# Clear all elements from a set using clear() and print it.
new_fruit.clear()
print(new_fruit)

# Delete a set completely using the del keyword and observe the result.
del a
print(a) #shows error
