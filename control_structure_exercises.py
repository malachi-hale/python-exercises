#1a
current_day = input("Please enter the day of the week.")

if current_day == 'Monday':
    print("Today is Monday!")
else: 
    print("Today is not Monday.")

#1b 
current_day = input("Please enter the day of the week.")
if current_day == 'Monday' or current_day == 'Tuesday' or current_day == 'Wednesday' or current_day == 'Thursday' or current_day == 'Friday':
    print("Today is a weekday.")
elif current_day == 'Saturday' or current_day == 'Sunday':
    print('Today is the weekend.')
else:
    print('Invalid date.')

#1c
number_of_hours_worked_in_a_week = input("How many hours did you work this week?")
hourly_rate = input("What is your hourly rate?")
number_of_hours_worked_in_a_week = int(number_of_hours_worked_in_a_week)
hourly_rate = int(hourly_rate)
if number_of_hours_worked_in_a_week <= 40:
    paycheck = hourly_rate * number_of_hours_worked_in_a_week
    print("You made", paycheck, "dollars this week.")
elif number_of_hours_worked_in_a_week > 40:
    paycheck = ((number_of_hours_worked_in_a_week - 40) * hourly_rate *1.5)+((((number_of_hours_worked_in_a_week)-(number_of_hours_worked_in_a_week-40))*hourly_rate))
    print("You made", paycheck, "dollars this week.")
else 
    print("You made money.")

#2a
i = 5
while (i <= 15): 
    print(i)
    i += 1
 
i = 0 
while(i <= 100):
    print(i)
    i += 2

i = 100
while(i >= - 10):
    print(i)
    i -= 5

i = 2
while(i <= 1000000):
    print(i)
    i = i*i

i = 100
while(i >= 5):
    print(i)
    i -= 5

#2bi 

