def foo(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    
    raise Exception("error")

if __name__ == "__main__":
    x, y = list(map(int, input().split()))
    print(foo(x, y))