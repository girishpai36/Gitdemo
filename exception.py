item=0
if item!=2:
    pass
    #raise Exception("requirement not met")
assert(item==2)

try:
    with open('file.txt' , 'r') as reader:
        reader.read()
except:
    print("this is execption from try block ")

