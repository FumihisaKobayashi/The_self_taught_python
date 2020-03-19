class Triangle():
    def __init__(self, wid, height):
        self.wid = wid
        self.height = height

    def calculate_area(self):
        return self.height * self.wid / 2

triangle = Triangle(20, 30)
print(triangle.calculate_area())