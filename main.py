class Notes:
    def __init__(self,title,content):
        self.__title = title
        self.__content = content


    def get_title(self) :
        return self.__title
    def get_content(self):
        return self.__content
Note1 = Notes("Note 1","This is the content of note 1") 

print(Note1.get_title())
print(Note1.get_content())  


numero = int(input("Enter a number: "))
for i in range (11):
    print (f"{numero} x {i} = {numero * i}")