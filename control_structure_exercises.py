#1a
current_day = input("Please enter the day of the week. ")

if current_day == 'Monday':
    print("Today is Monday!")
else: 
    print("Today is not Monday. ")
print("\n")
#1b 
current_day = input("Please enter the day of the week. ")
if current_day == 'Monday' or current_day == 'Tuesday' or current_day == 'Wednesday' or current_day == 'Thursday' or current_day == 'Friday':
    print("Today is a weekday.")
elif current_day == 'Saturday' or current_day == 'Sunday':
    print('Today is the weekend.')
else:
    print('Invalid date.')
print("\n")

#1c
number_of_hours_worked_in_a_week = input("How many hours did you work this week? ")
hourly_rate = input("What is your hourly rate? ")
number_of_hours_worked_in_a_week = int(number_of_hours_worked_in_a_week)
hourly_rate = int(hourly_rate)
if number_of_hours_worked_in_a_week <= 40:
    paycheck = hourly_rate * number_of_hours_worked_in_a_week
    print("You made", paycheck, "dollars this week.")
elif number_of_hours_worked_in_a_week > 40:
    paycheck = ((number_of_hours_worked_in_a_week - 40) * hourly_rate *1.5)+((((number_of_hours_worked_in_a_week)-(number_of_hours_worked_in_a_week-40))*hourly_rate))
    print("You made", paycheck, "dollars this week.")
else:
    print("You made money.")
print("\n")

#2a
i = 5
while (i <= 15): 
    print(i)
    i += 1
print("\n")

i = 0 
while(i <= 100):
    print(i)
    i += 2
print("\n")

i = 100
while(i >= - 10):
    print(i)
    i -= 5
print("\n")


i = 2
while(i <= 1000000):
    print(i)
    i = i*i
print("\n")

i = 100
while(i >= 5):
    print(i)
    i -= 5
print("\n")

#2bi 
user_number = int(input("Please enter a number:  \n"))

for i in range(1,10):
    product = user_number * i
    print(str(user_number), "x", str(i), "=", str(product))
print("\n")

#2bii
for i in range(1, 10):
    print(str(i) * i)
print("\n")

#2c
your_number = input("Please enter an odd number between 1 and 50: \n")

while your_number.isdigit() == False: 
    print("That was not a digit.")
    your_number = input("Please enter an odd number between 1 and 50: \n")

for i in range(1, 51):
    if i % 2 != 0 or i == int(your_number):
        if i == int(your_number):
            print("Yikes! Skipping number: ", i)
            continue
        print("Here is an odd number: ", i)
print("\n")

#2d 
new_number = input("Please enter a positive number: \n")
while new_number.isdigit() == False or int(new_number) <= 0: 
    print("That was not a valid positive number.")
    your_number = input("Please enter a valid positive number: \n")
i=0
while i <= int(new_number):
    print(i)
    i +=1
print("\n")

#2e 
positive_number = input("Please enter a positive integer: ")
while positive_number.isdigit() == False or int(positive_number) <= 0: 
    print("That was not a valid positive integer.")
    positive_number = input("Please enter a valid positive integer: \n")

i = int(positive_number) + 0
while i >=1: 
    print(i)
    i -= 1
print("\n")

#3
i  = 1
while i <= 100:
    if i%3 == 0 and i%5 != 0:
        print("Fizz")
    elif i%5 == 0 and i%3 != 0:
        print("Buzz")
    elif i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    else:
        print(i)
    i += 1 
print("\n")

#4 

user_integer = int(input("What number would you like to go up to? "))
print(f"\nHere is your table!\n")
print(f"number | squared | cubed")
print(f"------ | ------- | -----")

for i in range (1, user_integer + 1):
    print(f"{i:<7}|{i**2:<8} |{i**3:<4}")
    if user_integer <= i:
        break

go_up = input("Would you like to continue? ")
while go_up in ['yes']:
    user_integer = int(input("What number would you like to go up to? "))
    print(f"\nHere is your table!\n")
    print(f"number | squared | cubed")
    print(f"------ | ------- | -----")

    for i in range (1, user_integer + 1):
        print(f"{i:<7}|{i**2:<8} |{i**3:<4}")
        if user_integer <= i:
            break
print("\n")

#5
go_up = True
while go_up:
    your_grade = int(input("Please enter your numerical grade: "))
    if your_grade <= 100 and your_grade >= 99:
        print("A+")
    elif your_grade <= 98 and your_grade>= 90: 
        print("A")
    elif your_grade <= 89 and your_grade>= 88: 
        print("A-")
    elif your_grade <= 87 and your_grade>= 86: 
        print("B+")
    elif your_grade <= 85 and your_grade>= 82: 
        print("B")
    elif your_grade <= 81 and your_grade>= 80: 
        print("B-")
    elif your_grade <= 79 and your_grade>= 78: 
        print("C+")
    elif your_grade <= 77 and your_grade>= 68: 
        print("C")
    elif your_grade <= 68 and your_grade>= 67: 
        print("C-")
    elif your_grade <= 66 and your_grade>= 65: 
        print("D+")
    elif your_grade <= 64 and your_grade>= 62: 
        print("D")
    elif your_grade <= 61 and your_grade>= 60: 
        print("D-")
    elif your_grade <= 55 and your_grade >= 0:
        print("F")
    go_up = input("Would you like to keep going? ")
    if go_up not in ['yes']:
        go_up = False
print("\n")

#6
books = [
    {
    "Title": "Gone Girl", 
    "Author" : "Gillian Flynn",
    "Genre": "Thriller"
        },
    {
    "Title": "The Girl With the Dragon Tattoo",
    "Author": "Stieg Larsson",
    "Genre": "Mystery"
    }, 
    {
    "Title": "The Silent Patient",
    "Author": "Alex Michaelides",
    "Genre": "Slow Burn"
    }
]

your_genre = input("Please input the genre you want to read. The options are Thriller, Mystery, or Slow Burn:  ")
for book in books: 
    if your_genre == book["Genre"]:
        print(book)