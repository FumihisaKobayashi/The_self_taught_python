class Primo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_skill_1(self):
        print("死ぬ気の零地点突破FirstEdition")

#継承する親のことをsuper_classというこの場合super(Primo)

class Tsuna(Primo):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show_skill_2(self):
        print('死ぬ気の零地点突破改！')
#機能を引き継いで新しいclassをできる。

if __name__ == "__main__":
    primo = Primo('aaa', 24)
    primo.show_skill_1()

    print('*'*20)
    tsuna = Tsuna('bbb', '14')
    tsuna.show_skill_1()
    tsuna.show_skill_2()