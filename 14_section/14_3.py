class Rectangle:
     def __init__(self, w, l):
        self.width = w
        self.len = l
    
     def print_size(self):
        print("{} by {}".format(self.width, self.len))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

#classRectangle 変数recsを追加。
#__init__メソッドの外で行う。