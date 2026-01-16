class employee:
    def __init__(self, name, salary):
        self.name =  name
        print("Contructor is Called")

    def __del__(self):
        print("Destructor is called")

e = employee("Rahul", 25000)
