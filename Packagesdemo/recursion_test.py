def fact(x):
   fact = 1
   for i in range(1, x+1):
      fact*=i
   return fact

def rfact(x):
   if x==1:
      return 1
   else:
      return x*fact(x-1)
   
print ("Using loop:",fact(10))
print ("Using Recursion",rfact(10))

import timeit

setup1="""
from __main__ import fact
x = 10
"""

setup2="""
from __main__ import rfact
x = 10
"""

print ("Performance of factorial function with loop")
print(timeit.timeit(stmt = "fact(x)", setup=setup1, number=10000))

print ("Performance of factorial function with Recursion")
print(timeit.timeit(stmt = "rfact(x)", setup=setup2, number=10000))
