from pprint import pprint
pprint(dir(int))

print("========================================")
print("Dictionary containing the class's namespace.")
print(int.__dict__)

print("========================================")
print("Class documentation string or none, if undefined.")
print(int.__doc__)

print("========================================")
print("The name of the class.")
print(int.__class__)

print("========================================")
print("Module name in which the class is defined.This attribute is _main_ in interactive mode.")
print(int.__module__)

print("========================================")
print("A tuple containing the base classes,in the order of their occurrence in the base class list.")   
print(int.__bases__)

