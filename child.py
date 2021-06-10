from oopsdemo2 import Calculator
class ChildImp(Calculator):
    num2=200
    def __init__(self):
        Calculator.__init__(self,2,9)
    def getcompletedata(self):
        return self.num2+self.fn+self.sumataion()


obj=ChildImp()
print(obj.getcompletedata())