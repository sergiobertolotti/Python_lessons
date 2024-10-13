class Rettangolo(object):
    # attributi privati
    __base = 0.0
    __altezza = 0.0
    
    def assegna(self,b,h):
        self.__base = b
        self.__altezza = h
        
    def area(self):
        return self.__base * self.__altezza
    
    
def main():
    tovaglia = Rettangolo()
    tovaglia.assegna(5,3)
    print("Area = ", tovaglia.area())
    tovaglia.__base = 0
    print("Area =", tovaglia.area())
    
main()
            