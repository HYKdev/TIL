#####################
# public, protected, private

class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self): #public method
        return self.__age # private value

    def set_age(self): #public method
        self.__age += 1

tony = Person(27)
print(tony.get_age()) # 27

tony.set_age()
print(tony.get_age()) # 28

print(dir(tony))
#['_Person__age', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_age', 'set_age']


print(tony._Person__age) # 28
# 보여주는 용도지 사용 x

# name mangling

## getter, setter
class Person:
    def __init__(self):
        self.__age = None
        self.__name = None
    
    def __str__(self):
        return f"나이는 {self.__age}살 이구요, 이름은 {self.__name}입니다.!"
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # def get_name(self):
    #     return self.__name

    # def set_name(self, new_name):
    #     self.__age = new_name


aiden = Person()
aiden.set_age(24)

# aiden.set_name('aiden')
# aiden.get_name

aiden.name = 'aiden'
print(aiden.name)

aiden.name = 'jun'
print(aiden.name)
# method를 속성처럼 쓸 수 있다.

print(aiden)