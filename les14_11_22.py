class Person:
    def __init__(self,name,surname):
        self._name=name
        self._surname=surname
    def info(self):
        print("Name",self.name,"\nLast name", self.surname)
class Player(Person):
    def __init__(self, name, surname,team,kit_number,pos,stats):
        self._team = team
        self._kit_number = kit_number
        self._position = pos
        self._stats = stats
        
        Person.__init__(self,name,surname)
    def info(self):
        print("Name:",self._name,"\nLast name:", self._surname)
        print("Team:",self._team,"\Kit number:", self._kit_number,"\Position:", self._position,"\Stats:", self._stats)
        
        
Player1=Player("Jo","Vankuver","Mamai",22,"Foward", 0)


class Human:
    def __init__(self,name,surname, age,town):
        self._name=name
        self._surname=surname
        self._age=age
        self._town=town
    def display(self):
        print("Name",self.name,"\nLast name", self.surname,"\nAge", self.age,"\nTown", self.town)
        
            
class Student(Human):
    def __init__(self,name,surname, age,town,clas,dict ):
        self._clas = clas
        self._dict = dict
        
        Human.__init__(self,name,surname, age,town)
    def display(self):
        print("Name",self.name,"\nLast name", self.surname,"\nAge", self.age,"\nTown", self.town)
        print("Class:",self._clas,"\nDict:", self._dict)

def Math(a,b)
     
l1={
    "Math":5,
    "Eng":3,
    "IT":3    
    }
l2={
    "Math":2,
    "Eng":5,
    "IT":5    
    }
l3={
    "Math":2,
    "Eng":2,
    "IT":2    
    }
l4={
    "Math":4,
    "Eng":3,
    "IT":5    
    }
l5={
    "Math":4,
    "Eng":4,
    "IT":5    
    }
h1=Student("Jo","Jo", 8,"Moscow", 3, l1)
h2=Student("Li","Li", 9,"NiNo", 4, l2)
h3=Student("Ni","Li", 11,"Mahachkala", 6, l3)
h4=Student("San","Li", 6,"Yfa", 1, l4)
h5=Student("Re","Li", 7,"Omsk", 2, l5)

h3.display()