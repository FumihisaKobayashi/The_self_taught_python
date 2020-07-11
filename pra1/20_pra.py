class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

#Orangeクラスを利用して複数のオブジェクト制作。
or1 = Orange(4, "Light orange")
or2 = Orange(8, "dark Orange")
or3 = Orange(14, "yellow")

#0r1,or2....でclassを追加.

print(or1.weight)
print(or1.color)