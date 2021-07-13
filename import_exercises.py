from function_exercises1 import calculate_tip
print(calculate_tip(0.2, 100))

import itertools
print(list(itertools.product("abc", [1,2,3])))
print(len(list(itertools.product("abc", [1,2,3]))))

print(list(itertools.combinations("abcd",2)))
print(len(list(itertools.combinations("abcd",2))))

print(list(itertools.permutations("abcd",2)))
print(len(list(itertools.permutations("abcd",2))))

import json
my_file = json.load(open('profiles.json'))
print(len(my_file))

active_users = 0
for my_user in my_file:
    if my_user["isActive"] == True:
        active_users += 1

print(active_users)

inactive_users = 0
for my_user in my_file:
    if my_user["isActive"] == False:
        inactive_users += 1
print(inactive_users)

balances = []
for my_user in my_file:
    balances.append(my_user["balance"])
new_balances=[]
for balance in balances:
    balance = balance.lstrip("$")
    balance = balance.replace(",", "")
    new_balances.append(balance)
balance_float = []
for new_balance in new_balances:
    new_balance = float(new_balance)
    balance_float.append(new_balance)
print(sum(balance_float))

average_balance = sum(balance_float) / (len(my_file))
print(average_balance)

balance1 = []
for my_user in my_file:
    balance1.append(my_user["balance"])
for my_user in my_file:
    if my_user["balance"] == max(balance1):
        print(my_user["name"])

balance2 = []
for my_user in my_file:
    balance2.append(my_user["balance"])
for my_user in my_file:
    if my_user["balance"] == min(balance2):
        print(my_user["name"])

fruit_types = dict()
for my_user in my_file:
    if my_user["favoriteFruit"] in fruit_types.keys():
        fruit_types[my_user["favoriteFruit"]] += 1
    else:
        fruit_types[my_user["favoriteFruit"]] = 1
print(max(fruit_types))
print(min(fruit_types))


for my_user in my_file:
    for greeting in my_user["greeting"]: 
        just_numbers = ''.join(i for i in greeting if i.isdigit())
        print(just_numbers)

    

