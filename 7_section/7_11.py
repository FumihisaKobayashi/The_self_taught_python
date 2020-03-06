list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []


#list1とlist2の和の表記(addedに追加)一個めi 二個目j
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

