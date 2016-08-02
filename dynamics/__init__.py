# create a method for a dynamis
class Dynamics:
    def __init__(self):
        self.nm_model = []
        self.models = {}

    def add_nm_model(self, module):
        self.nm_model.append(module)

    def add_model(self, nm_model, status):
        self.models[nm_model] = status

    def get_lst_nm_models(self):
        return self.nm_model

    def get_models(self):
        return self.models

# create a method for each model
class Model:
    def __init__(self, name, d_rls, lst_ams):
        self.name = name
        self.rls = d_rls
        self.lst_ams = lst_ams

    def getname(self):
        return self.name

    def getD(self):
        return self.rls

    def getL(self):
        return self.lst_ams