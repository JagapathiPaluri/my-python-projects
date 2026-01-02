from timeit import timeit
time = timeit('[n*2 for n in range(100)]', number=10000)
print(time)

string = '''num=[]
for n in range(100):
      num.append(n*2)'''
time2 = timeit(string, number=10000)
print(time2)