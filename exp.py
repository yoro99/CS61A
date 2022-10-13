def func(n):
    i = 0
    while i < n:
        yield i
        i += 1
    yield StopIteration
print("debug1")
for x in func(5):
    print(x)
print("debug2")