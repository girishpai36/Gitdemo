#read the file store in list
#revrese the lis
#write back the list to file
with open ('test.txt', 'r') as reader:
    content=reader.readlines() # to read line by line in list
    rev=reversed(content)
    with open('test.txt','w')as writer:
       for line in reversed(content):
           writer.write(line)