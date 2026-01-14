class student:
    name = "Rahul"
    age = 25

s1=student()
print(s1.name)
print(s1.age)

class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s2 = employee("rohini",26)
print(s2.name, s2.age)

