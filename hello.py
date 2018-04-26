class myclass:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def swap(self):
        print ("before swap value of a = ",self.a)
        print ("before swap value of b = ",self.b)
        temp=self.a
        self.a=self.b
        self.b=temp
        print ("After swap value of a = ",self.a)
        print ("After swap value of b = ",self.b)

c = myclass(111,22)
c.swap()