class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.x2 = int(input('enter the value for x1: '))
        self.y2 = int(input('enter the value for y1: '))
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def setx(self):
        self.x=x1
    def sety(self):
        self.y=y1
    def display(self):
        print('first point object: (' + str(self.x) + ', ' + str(self.y) + ') second point object: (' + str(
            self.x2) + ',' + str(self.y2) + ')')

    def distance(self):
        xcor_calc = (self.x - self.x2) ** 2
        ycor_calc = (self.y - self.y2) ** 2
        dist_calc = (xcor_calc + ycor_calc) ** (1 / 2)
        return dist_calc

a=int(input("Enter the value of x:"))
b=int(input("Enter the value of y:"))
p1= Point(a,b)
p1.display()
print('The distance between first point object and second point object is: ', p1.distance())
