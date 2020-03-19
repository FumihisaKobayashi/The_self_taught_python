#[クラス名]([引数])
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

or1 = Orange(10, "dark orange")
print(or1)

#クラスを定義してからOrange[class](10, "dark orange")のコードでインスタンス化