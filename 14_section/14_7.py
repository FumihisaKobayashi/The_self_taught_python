

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

#isは、前後のオブジェクトが同一のオブジェクトならTrueを返す。違うならFalseを返す。


another_bob = Person()
print(bob is another_bob)

