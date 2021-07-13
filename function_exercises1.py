def is_vowel(n):
    if n.lower() in 'aeiou':
        return True
    else:
        return False 

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