
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.tems) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
print(stack.is_empty())

#あたらしい要素を追加すると is_emptyは FALSEを返す。