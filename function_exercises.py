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
        return "not a word" 
    else:
        return "not a single word"

print(capitalize("bananas"))
print(capitalize("apple"))
print(capitalize("hello"))
print(capitalize(9))
print(capitalize("I love potatoes"))
print("\n")

#5
def calculate_tip(tip, bill):
    if type(tip) == str or type(bill) == str:
        return "Not a number"
    elif type(tip) == float or int and type(bill)==float or int:
        if tip < 0 or tip > 1:
            return "This tip amount is not between 0 and 1."
        elif tip >= 0 and tip <= 1:
           return tip * bill 
    else: 
        return print("Invalid")
print(calculate_tip(0.2, 100))
print(calculate_tip(1.1, 60))
print(calculate_tip("potatoes", "bananas"))
print("\n")
#6 
def apply_discount(price, discount):
    if type(price) == str or type(discount) == str:
        return "Not a number"
    elif type(price) == float or int and type(discount)==float or int:
        return (price) - (price * discount)

print(apply_discount(100, 0.2))
print(apply_discount(60, 0.5))
print(apply_discount("potatoes", "bananas"))
print("\n")

#7
def handle_commas(number):   
    if type(number) == str: 
         new_number = number.replace(',', "")
         return new_number 
    elif type(number) == float or int:
        return number

print(handle_commas("9,000"))
print(handle_commas("8,000,000"))
print(handle_commas(9000))
print(handle_commas("potatoes"))
print("\n")

#8 
def get_letter_grade(grade):
    if type(grade) == str:
        return "Not a valid number grade."
    elif type(grade) == float or int:
        if grade <= 100 and grade >= 90:
            return "A"
        elif grade <= 89 and grade >= 80:
            return "B"
        elif grade <= 79 and grade >= 70:
            return "C"
        elif grade <= 69 and grade >= 60:
            return "D"
        elif grade <= 59:
            return "F"
   

print(get_letter_grade(99.9))
print(get_letter_grade(70))
print(get_letter_grade(0))
print(get_letter_grade("bananas"))
print("\n")

#9
def remove_vowels(word):
    if type(word) == str:
        for i in word.lower():
            if i in ('a', 'e', 'i', 'o', 'u'):
                word=word.replace(i, "")
        return word
    elif type(word) == int or float: 
        return "not a valid word"

print(remove_vowels("bananas"))
print(remove_vowels("Today I went to the mall and saw my friend"))
print(remove_vowels(9000))
print("\n")
#10 
def normalize_name(name):
    if type(name) == str:
        if name.isnumeric():
            return "unable to normalize names made entirely out of numbers"
        else:
            name = name.lower()
            for i in name:          
                if i.isalpha() == False and i.isnumeric() == False:
                    name = name.replace(i, " ") 
            name = name.strip()
            for i in name:
                name = name.replace("  ", " ")
            name = name.replace(" ", "_")
            if not name:
                return "The string is made entirely out of symbols"
            else:
                while name[0].isnumeric():
                    name = name[1:]
                return name
    elif type(name) == float or int:
        return "not a string"

print(normalize_name("Today I went to the store"))
print(normalize_name("%      words hello"))
print(normalize_name("Today I % $"))
print(normalize_name("999999%9_a9asdlk"))
print(normalize_name("9000"))
print(normalize_name("$#$"))
print(normalize_name("1 2 3 $()&^$( T#%^H#%^i%^s%^ i%^&S %&(*(a v$%&AlI#%^d p#%^YTh#%^on id#%^%&en$%&TI#$^%%$&^*Fi@$%^*(er  #^#^#@"))
print("\n")

#11
def cumulative_sum(list):
    cumulative_list = []
    i =0 
    for j in range(0, len(list)):
        i += list[j]
        cumulative_list.append(i)
    return cumulative_list

list = [10, 20, 30, 40, 50]
print(cumulative_sum(list))
print("\n")

#Bonus 1 
def twelveto24(time):
    if time[-2:] == "am" and time[:2] == "12":
            return "00" + time[2:-2]
    elif time[-2:] == "am":
        return time[:-2]
    elif time[-2:] == "pm" and time[:2] == "12":
        return time[:-2]
    elif len(time) == 6 and time[-2:] == "pm":
        return str(int(time[:1])+12) + time[1:-2]
    elif len(time) == 7 and time[-2:] == "pm":
        return str(int(time[:2])+12) + time[2:-2]

print(twelveto24("10:45am"))
print(twelveto24("4:30pm"))
print(twelveto24("12:30pm"))

def col_index(letters):
    if len(letters) >= 2:
        numbers = []
        i = 0
        while i < len(letters):
            value = (25 * i) + ord(letters[i]) - 64
            numbers.append(value)
            i += 1
        return sum(numbers)
    elif len(letters) == 1:
        numbers1= ""
        letter_number = ord(letters) - 64
        numbers1 += str(letter_number)
        return numbers1 

print(col_index('A')) 
print(col_index('B'))
print(col_index('AA'))
print(col_index('BB'))
