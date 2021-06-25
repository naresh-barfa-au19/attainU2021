
class Animal:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Animal class ")
        print("name ",self.name)

class Wild:
    def __init__(self,breed):
        self.breed = breed
    def display(self):
        print("wild class ")
        print("name ",self.breed)

class loin(Animal,Wild):
    def __init__(self, name,breed):
        Animal.__init__(self,name)
        Wild.__init__(self,breed)

    # def display(self):
    #     print("loin class ")
    #     print("name  and breed ",self.name,self.breed)

loin1 = loin("simba","cat family")

loin1.display()