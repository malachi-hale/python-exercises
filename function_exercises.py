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
    if type(n) == str:
        if n[0] in 'bcdfghjklmnpqrstvwxyz':
            return n.capitalize()
        elif n[0] in 'aeiou':
            return n
    else:
        return print("not a word")

print(capitalize("bananas"))
print(capitalize("apple"))
print(capitalize("hello"))
print(capitalize(9))