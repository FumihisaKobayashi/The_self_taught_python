class student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#他で開くときに実行（表記されないようにする。）
if __name__ =="__main__":
    student = student("fumihisa", "24", "man")
    

#インスタンスがクッキー、　CLASSがクッキーの型の例。classのなかに情報入れていく,
#辞書と違うところは、参照できるところ。