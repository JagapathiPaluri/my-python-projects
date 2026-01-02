def multiplier(a):  
   # Nested function with second number   
   def multiply(b):
      # Multiplication of two numbers  
      return a * b 
   return multiply   

# Assigning nested multiply function to a variable  
multiply_second_number = multiplier(5)  
# Using variable as high order function  
Result = multiply_second_number(10) 
result2 = multiply_second_number(20)  
# Printing result  
print("Multiplication of Two numbers is: ", Result) 
print("Multiplication of Two numbers is: ", result2) 