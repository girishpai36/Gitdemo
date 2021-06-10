class Calculator:
    def __init__(self,a,b):
        self.fn=a
        self.sn=b
        print("constructor")


    def sumataion(self):
        return self.fn+self.sn


#obj1=Calculator(3,4)
#print(obj1.sumataion())