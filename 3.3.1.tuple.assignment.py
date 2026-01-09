# Create a tuple named 'fruits' containing five fruit names and print it.
fruits=("apple","banana","chiku","cherry","papaya")
print(fruits)

# Create a tuple with mixed data types (string, integer, float, boolean) and display each element using indexing.
mixed=(1,1.2,"apple", True)
print(mixed[0])
print(mixed[1])
print(mixed[2])
print(mixed[3])

# Access the last element of a tuple using negative indexing.
print("last element:",fruits[-1])

# Slice a tuple to print only the first three elements.
print("first three elements:",fruits[0:3])

# Use len() to find the number of elements in a tuple named 'students'.
students=("a","b","c","d","e")
print("length of tuple students:",len(students))

# Use max() and min() to find the highest and lowest marks from a tuple of integers.
marks=(1,2,34,56,7,4,27,4)
print("highest marks",max(marks))
print("lowest marks",min(marks))

# Use sum() to calculate the total sales from a tuple of daily sales data.
daily_sales=(23,45,7654,457,654,4565,356)
print("total sales of today:",sum(daily_sales))

# Sort a tuple of numbers in ascending order using sorted() and convert it back to a tuple.
sorted_num=tuple(sorted(marks))
print("sorted numbers in ascending order:",sorted_num)

# Sort a tuple of numbers in descending order using sorted() with reverse=True.
des_sorted_num=tuple(sorted(marks,reverse=True))
print("sorted numbers in descending order:",des_sorted_num)

# Count how many times a specific value appears in a tuple using the count() method.
print("count of a particular number 23:",daily_sales.count(23))

# Find the index of a specific element in a tuple using the index() method.
print("index of 2 is",marks.index(2))

# Check if "Python" is present in a tuple using the 'in' keyword.
print("is python present true or false?","python" in marks)

# Check if "C++" is not present in a tuple using the 'not in' keyword.
print("is c++ present true or false?","c++" in marks)

# Create a tuple from a range of numbers 1 to 10 using the tuple() and range() functions.
tuple_range=tuple(range(1,10))
print(tuple_range)

# Use any() on a tuple of boolean values to check if at least one element is True.
boolean=(1,1,1,1)
print("at least one element is True or not:",any(boolean))

# Use all() on a tuple of boolean values to check if all elements are True.
print("all elements are True or not:",all(boolean))

# Concatenate two tuples representing first names and last names.
first=("rutu")
last=("patil")
full=first+last
print("full name:",full)

# Repeat a tuple containing ("AI", "ML") three times using the * operator.
repeat=("ai","ml")
print("printing tuple 3 times",repeat*3)

# Combine two tuples (names and scores) using zip() and convert the result into a tuple.
name=("rutu","raj")
scores=(50,40)
zipped=tuple(zip(name,scores))
print("zipped names and scores:", zipped)

# Reverse a tuple using the reversed() function and convert it back to a tuple.
print("reversed tuple is",tuple(reversed(name)))

# Find the alphabetically first and last element in a tuple of strings using min() and max().
string1=("abc","mno","pqr","xyz")
print("first element is",min(string1))
print("last element is",max(string1))

# Unpack a tuple of three elements into three separate variables and print them.
stock=("reliance",1900, 20)
name,price,pe=stock
print("name of stock:",name)
print("current price of stock:",price)
print("price to earning ratio of stock:",pe)

# Create a tuple of 10 numbers and calculate the average using sum() and len().
numbers1=(1,2,3,4,5,6,7,8,9,0)
print("average of numbers:",sum(numbers1)/len(numbers1))

# Create a tuple of city names and print them in reverse order using slicing.
city_names=("nanded","pune","mumbai","nashik","nagpur")
print("reverse order of cities",city_names[::-1])

# Convert a tuple of numbers into a list, append a new number, and convert it back into a tuple.
num_list=list(numbers1)
print(num_list)
num_list.append(20)
print(num_list)
back_tuple=tuple(num_list)
print(back_tuple)

# Create a tuple of employee details (Name, Age, Department) and use unpacking to print each value separately.
employee=("johan",20,"marketing")
print(employee)
name,age,department=employee
print("name:",name)
print("age:",age)
print("department:",department)

# Create two tuples — (product_name, price) — and combine them using zip(); then display them sorted by price in descending order.
product_name=("soap","brush","bottle","charger")
price=(20,15,30,200)
combined=tuple(zip(product_name,price))
print(sorted(combined))

# Compare the memory size of a list and a tuple containing the same elements using sys.getsizeof().
list2=[1]
tuple2=(2)
print(sys.getsizeof(list2))
print(sys.getsizeof(tuple2))

# Create a tuple and demonstrate immutability by trying to modify an element (observe the error).
string1[0]="apple"
print("immutable checking",string1)

# Create a nested tuple that stores a country name and its states as another tuple.
nested_tuple=("india",("goa","delhi","punjab"))
print(nested_tuple[0])
print(nested_tuple[1,0])