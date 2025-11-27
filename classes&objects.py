class Fruits:
    def __init__(self, name, size, color):
        self.n=name
        self.s=size
        self.c=color
        self.r=0
    def showdetails(self):
        print(self.n,self.s, self.c, self.r)
    def changerating(self):
        self.r =int(input("Enter the rating: "))

apple = Fruits("apple", "medium", "red")
apple.changerating()
apple.showdetails()

olive = Fruits("olive", "small", "green")
olive.changerating()
olive.showdetails()