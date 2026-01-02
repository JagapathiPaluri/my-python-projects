def func(f):
    def wrapper(*args, **kwargs):
        print("stated")
        rv = f(*args, **kwargs)
        print("ended")
        return rv
    return wrapper

#@func
def func2(x,y):
    print(x)
    print(y)
    return x + y

func2 = func("func2")


g = func2(5,6)
print(g)


     