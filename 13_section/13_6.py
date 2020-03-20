class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

#Squareの中にShapeを指定して継承
class Square(Shape):
    pass
#passはpythonに何もしなくて良いこと伝えている

a_square = Square(20, 20)
a_square.print_size()
#親クラスには影響しない。