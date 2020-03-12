my_list = []

with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)