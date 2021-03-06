
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


#popメソッドはスタックから要素を取り除くので、is_emptyは再びTRUEを返す。
stack = Stack()
stack.push(1)
item = stack.pop()
print(item)
print(stack.is_empty())

