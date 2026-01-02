from pprint import pprint
pprint(dir(object))


print("Dictionary containing the class's namespace.")
print(object.__dict__)

print("Class documentation string or none, if undefined.")
print(object.__doc__)

print("The name of the class.")
print(object.__class__)

print("Module name in which the class is defined.This attribute is _main_ in interactive mode.")
print(object.__module__)

print("A tuple containing the base classes,in the order of their occurrence in the base class list.")   
print(object.__bases__)

