class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
print(lion)

#__repr__ インスタンス変数を返す。
