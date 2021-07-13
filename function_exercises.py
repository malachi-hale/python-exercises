#1
def is_two(n):
    if n == 2 or n == "2":
        return True 
    else: 
        return False

print(is_two(2))
print(is_two("2"))
print(is_two(1000))
print("\n")

#2
def is_vowel(n):
    if n.lower() in 'aeiou':
        return True
    else:
        return False 

print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel("c"))
print("\n")

#3
def is_consonant(n):
    if n.lower() in 'bcdfghjklmnpqrstvwxyz':
        return True
    else:
        return False 
print(is_consonant("a"))
print(is_consonant("b"))
print(is_consonant("c"))
print("\n")

#4
def capitalize(n):
    if type(n) == str and n.isalpha() == True:
        if n[0] in 'bcdfghjklmnpqrstvwxyz':
            return n.capitalize()
        elif n[0] in 'aeiou':
            return n
    elif type(n) != str:
        return print(n, "is not a word"), n 
    else:
        return print(n, "is not a single word"), n 

print(capitalize("bananas"))
print(capitalize("apple"))
print(capitalize("hello"))
print(capitalize(9))
print(capitalize("I love potatoes"))
print("\n")

#5
def calculate_tip(tip, bill):
    if type(tip) == str or type(bill) == str:
        return print("Not a number")
    elif type(tip) == float or int and type(bill)==float or int:
        if tip < 0 or tip > 1:
            return print("This tip amount is not between 0 and 1.")
        elif tip >= 0 and tip <= 1:
           return tip * bill 
    else: 
        return print("Invalid")
print(calculate_tip(0.2, 100))
print(calculate_tip(1.1, 60))
print(calculate_tip("potatoes", "bananas"))

