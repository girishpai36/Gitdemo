try:
    with open('file.txt' , 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("it executes every time with out dependening on try catchs")