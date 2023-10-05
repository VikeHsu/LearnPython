from Car import car

#定义 civic 类
class civic(car):
    def __init__(self,color):
        super().__init__('Honda',"Civic")
        self.color = color
    
    def print(self):
        print(self.make  + ' ' + self.model + ' ' + self.color)
