
#inputのコロン注意。
a = input("Type a number:")
b = input("Type anothet:")
a = int(a)
b = int(b)


#例外処理,try,except

try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero")
