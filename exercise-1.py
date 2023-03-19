henry_list = [1, 2, 4, 4, 2, 3, 4, 3]
new_list = []
for i in henry_list:
    if henry_list.count(i) > 1 and i not in new_list:
        new_list.append(i)
        print(i)
if len(henry_list) == 0 or len(new_list) == 0:
    print(None)


