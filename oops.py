##class myclass:
##    x=5
##print(myclass)

##class rect:
## l=5
## b=8
##print("area of rectangle:",(rect.l*rect.b))

class rect:
    def __int__(self):
        self.l=8
        self.b=5
    def rectarea(self):
        return self.l*self.b
class triangle(rect):
    def __init__(self):
        rect.__init__(self)
        self.x=10
        self.y=40
    def triarea(self):
        return 1/2*self.x*self.y
r=triangle()
print("area of rectangle is",r.rectarea())
print("area of triangle is",r.triarea())
