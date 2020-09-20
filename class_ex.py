class Point:
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
    def move(self):
        print('move')
    def draw(self):
        print('draw')
point1 = Point(2,3)
point1.draw()
point1.move()
#point1.x = 0
#point1.y = 1
print(point1.x)
print(point1.y)

class Person:
    def __init__(self,name):
        super().__init__()
        self.name = name
    def talk(self):
        print(self.name + "  talks !!" )

person = Person('Teja')
person.talk() 
