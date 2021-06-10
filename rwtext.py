file=open('test.txt')
#  print(file.read(7))
#print(file.readline())
#print(file.readline())
#print line by line using redaline method interview question
line=file.readline()
while line!="":
    print(line)
    line=file.readline()
file.close()
file1=open('test.txt')
for line1 in file1.readlines():
    print(line1)