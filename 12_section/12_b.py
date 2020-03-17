#
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
#classのなかに、関数を入れていく。
    def add_age(self, num):
        self.age += num

    def show_name(self):
        print('君の名前は' + self.name)

#Student(2)でclass代用可能
if __name__ == "__main__":
    student = Student('kosuke', 24, 'M')
    student2 = Student('fumihisa', 24, 'M')

    room = [student, student2]

    for s in room:
        s.show_name()