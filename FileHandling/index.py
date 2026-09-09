with open("FileHandling/index.txt", "a+") as file:
    content = file.read() ; 
    file.write("new line added throuhg pythonn file module ")


with open('FileHandling/index.text' , 'r') as file : 
    content = file.read()
print(content)