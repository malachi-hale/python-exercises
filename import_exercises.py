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

def find_active_users(my_file):
    active_users = 0
    for my_user in my_file:
        if my_user["isActive"] == True:
            active_users += 1
    return active_users

def find_inactive_users(my_file):
    inactive_users = 0
    for my_user in my_file:
        if my_user["isActive"] == False:
            inactive_users += 1
    print(inactive_users)

def find_average_balance(my_file):
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
    average_balance = sum(balance_float) / (len(my_file))
    return(average_balance)

def find_user_with_max_balance(my_file):
    balance1 = []
    for my_user in my_file:
        balance1.append(my_user["balance"])
    for my_user in my_file:
        if my_user["balance"] == max(balance1):
            return my_user["name"]

def find_user_with_min_balance(my_file):
    balance2 = []
    for my_user in my_file:
        balance2.append(my_user["balance"])
    for my_user in my_file:
        if my_user["balance"] == min(balance2):
            return my_user["name"] 

def find_max_fruit_types(my_file):
    fruit_types = dict()
    for my_user in my_file:
        if my_user["favoriteFruit"] in fruit_types.keys():
            fruit_types[my_user["favoriteFruit"]] += 1
        else:
            fruit_types[my_user["favoriteFruit"]] = 1
    return max(fruit_types)

def find_min_fruit_types(my_file):
    fruit_types = dict()
    for my_user in my_file:
        if my_user["favoriteFruit"] in fruit_types.keys():
            fruit_types[my_user["favoriteFruit"]] += 1
        else:
            fruit_types[my_user["favoriteFruit"]] = 1
    return min(fruit_types)

def find_total_unread_messages(my_file):
    running_total = 0
    for my_user in my_file:
        numbers = ""
        for char in my_user["greeting"]:
            if char.isdigit() == True: 
                numbers += char 
        numbers = int(numbers)
        running_total += numbers
    return running_total

    

