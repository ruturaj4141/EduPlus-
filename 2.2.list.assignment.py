# Create a list of 10 numbers and print the list.
# Create a list containing different data types (integer, float, string, boolean) and print its type.
# Access and print the first, middle, and last elements from a list of your choice.
# Slice the list to print the first 3 elements and last 3 elements separately.
# Replace the second element of a list with a new value.
# Add a new element at the end of a list using append() and display the updated list.
# Insert an element at index 2 using insert() and print the updated list.
# Extend the list with another list of your choice and display the final list.
# Remove a specific element by value using remove() and display the result.
# Remove the element at index 3 using pop() and display which element was removed.
# Delete the element at index 0 using del keyword and print the remaining list.
# Clear all elements from the list using clear() and print the empty list.
# Recreate a list and check whether a specific element (for example "apple") exists in the list using the in operator.
# Find the index position of a specific element in the list using the index() method.
# Count how many times a specific value appears in the list using count().
# Sort a list of numbers in ascending order using sort() and display the result.
# Sort a list of strings in descending order using sort(reverse=True) and display the result.
# Reverse the order of a list using reverse() and print the updated list.
# Copy the contents of one list to another using the copy() method and modify one list to see if it affects the other.
# Combine two lists using the + operator and print the combined list.

# Create a list of 10 numbers and print the list.
number=[1,4,8,2,5,7,9,0,3,6]
print(number)

# Create a list containing different data types (integer, float, string, boolean) and print its type.
mixed_list=[1,2,"apple",6.65,True]
print(mixed_list)
print(type(mixed_list))

# Access and print the first, middle, and last elements from a list of your choice.
print(number[0])
print(number[-1])
middle_index=len(number)//2
middle_element=number[middle_index]
print(number[middle_element])

# Slice the list to print the first 3 elements and last 3 elements separately.
print(number[0:3])
print(number[-3:])

# Replace the second element of a list with a new value.
number[1]=25
print(number)

# Add a new element at the end of a list using append() and display the updated list.
number.append(30)
print(number)

# Insert an element at index 2 using insert() and print the updated list.
number.insert(2,445)
print(number)

# Extend the list with another list of your choice and display the final list.
my_list=[23,45,78,98,42]
number.extend(my_list)
print(number)

# Remove a specific element by value using remove() and display the result.
number.remove(23)
print(number)

# Remove the element at index 3 using pop() and display which element was removed.
number.pop(3)
print(number)

# Delete the element at index 0 using del keyword and print the remaining list.
del number[0]
print(number)

# Recreate a list and check whether a specific element (for example "apple") exists in the list using the in operator.
print(5 in number)
print(92 not in number)

# Find the index position of a specific element in the list using the index() method.
print(number.index(9))

# Copy the contents of one list to another using the copy() method and modify one list to see if it affects the other.
copied_list=number.copy()
print(copied_list)
copied_list.insert(0,99)
print(copied_list)
print(number)


# Sort a list of numbers in ascending order using sort() and display the result.
unsorted=[34,64,23,78,90,1,56]
print(unsorted.sort())

# Sort a list of strings in descending order using sort(reverse=True) and display the result.
print(unsorted.sort(reverse=True))

# Reverse the order of a list using reverse() and print the updated list.
print(number.reverse())

# Count how many times a specific value appears in the list using count().
print(number.count(5))

# Combine two lists using the + operator and print the combined list.
new_list= number + unsorted
print(new_list)

# Clear all elements from the list using clear() and print the empty list.
number.clear()
print(number)

