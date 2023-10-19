class First(object):
    def __init__(self, number):
        print("first", number)

class Second(First):
    def __init__(self):
        super().__init__(2)
        print("second")

class Third(First):
    def __init__(self):
        super().__init__(3)
        print("third")

class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        #super(Third, self).__init__()
        print("that's it")

fourth = Fourth()
