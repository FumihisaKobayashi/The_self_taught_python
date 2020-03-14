a = input("明日は何曜日ですか？")

with open("week.txt", "w") as f:
    f.write(a)
    
