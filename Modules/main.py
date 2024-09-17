# Import the user-defined module
import mymodule

# Use the functions and variables from the module (mymodule)
name = "Alice"
greeting = mymodule.greet(name)
print(greeting)

#using the add function
result = mymodule.add(10, 10)
print(f"10 + 10 = {result}")