try:
    a = input("Type a number:")
    b = input("Type anothet:")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")

    #複数例外処理する時は　, で区切る。