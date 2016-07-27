class Dynamics:
    def __init__(self):
        self.nObject = []
        self.d_Object = {}

    def addnObject(self, objct):
        self.nObject.append(objct)

    def addd_Object(self, key, value):
        self.d_Object[key] = value

    def getnObject(self):
        return self.nObject

    def getd_Object(self):
        return self.d_Object

    def shownmObjects(self):
        for o in self.nObject:
            return o

    def __str__(self):
        return "name object is : " + str(self.nObject) + "\n dictionary object is : " + str(self.d_Object)


def f_example():
    print("this is from init file")