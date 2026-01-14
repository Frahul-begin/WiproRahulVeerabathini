def add(a, b):
    print(a+b)

def subtract(a, b):
    return a - b

add(2, 3)
print(subtract(50, 30))

def hello(greeting= 'Hello', name='world'):
    print('%s, %s!'%(greeting, name))

hello()
hello('Greeting')
hello(greeting='MR', name='Rahul')

def print_param(*params):
    print(params)

print_param(1,2,3)
print_param('Python Testing')

def print_param1(**params):
    print(params)

print_param1(x=1, y=2, z=3)