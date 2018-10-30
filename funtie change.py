
def change(list):
    list.clear()
    list_new = ['d', 'e', 'f']
    for i in len(list_new):
        list_new = list.append(list_new[i])
        print(list_new)


list = ['a', 'b', 'c']
print(list)
print(change(list))
