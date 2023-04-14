class Phone:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def Call(self,number):
        print("you are calling this number")

iphone=Phone("I phone 14 pro max","black")
iphone.Call("0769694842")