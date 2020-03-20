class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

#承継して新しい句上書きをメソッドオーバーライド
class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size
