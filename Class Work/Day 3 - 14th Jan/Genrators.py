def numbers():
    yield 10
    yield 20
    yield 30
gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

def count_up(n):
    for i in range(1, n+1):
        yield i

for val in count_up(5):
    print(val)