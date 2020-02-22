
colors = ["purple", "orange", "green"]

#例文通りやろうとすると、日本語だと反応しない、、分からない、、確認。
guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")