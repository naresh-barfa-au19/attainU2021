class A:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("inside class A",self.name)

class B(A):
    def __init__(self,name):
        self.name = name
        super().__init__(name)

    # def display(self):
    #     print("inside class B",self.name)

class C(B):
    def __init__(self,name):
        self.name = name
        super().__init__(name)

    # def display(self):
    #     print("inside class C",self.name)

xyz = C("Naresh")
xyz.display()
