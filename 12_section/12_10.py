class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

#areaメソッドにて２つのインスタンス定数lenとwidthをかけてRectangleでオブジェクトの面積を返す
    def area(self):
        return self.width * self.len

#change_sizeでメソッドに代入して変更
    def change_size(self, w, l):
        self.width = w
        self.len = l


rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
