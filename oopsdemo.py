class basic:
    def __init__(self):
        print("this constrictor method and called autimatically")

        
    def getdata(self):
        print(" this is getdata method inside class")

    num=100

obj=basic()
obj.getdata()
print(obj.num)