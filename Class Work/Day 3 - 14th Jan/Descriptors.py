class mydescriptor:
    def __get__(self, obj, owner):
        print("Getting value")
        return obj._x

    def __set__(self, obj, value):
        print("Setting the value")
        obj._x = value

class Test:
    x= mydescriptor()
t = Test()
t.x=10
print(t.x)