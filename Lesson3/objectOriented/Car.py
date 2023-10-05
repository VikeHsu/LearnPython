
#定义汽车类：
class car:
    def __init__(self, make = '', model = ''):
        self.make = make
        self.model = model
        self.milage = 0

    def set_make(self, make):
        self.make = make

    def get_make(self):
        return self.make

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def drive(self,miles):
        self.milage += miles

    def get_milage(self):
        return self.milage
