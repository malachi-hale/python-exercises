fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

#Exercise 1
uppercased_fruit = [fruit.upper() for fruit in fruits]
print(uppercased_fruit)

#Exercise 2 
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

#Exercise 3
fruit_with_more_than_two_vowels = [x.lower() for x in fruits if x.count('a') + x.count('e') + x.count('i') + x.count('o')+ x.count('u') > 2]
print(fruit_with_more_than_two_vowels)

#Exercise 4 
fruit_with_only_two_vowels = [x.lower() for x in fruits if x.count('a') + x.count('e') + x.count('i') + x.count('o')+ x.count('u') == 2]
print(fruit_with_only_two_vowels)

#Exercise 5
fruits_with_more_than_five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print(fruit_with_more_than_two_vowels)

#Exercise 6
fruits_with_exactly_five_characters = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_exactly_five_characters)

#Exercise 7 
fruits_with_less_than_five_characters = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_five_characters)

#Exercise 8 
number_of_characters_in_each_fruit = [len(fruit) for fruit in fruits]
print(number_of_characters_in_each_fruit)

#Exercise 9 
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

#Exercise 10 
even_numbers = [number for number in numbers if number%2 ==0]
print(even_numbers)

#Exercise 11 
odd_numbers = [number for number in numbers if number%2 !=0]
print(odd_numbers)

#Exercise 12
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

#Exercise 13
negative_numbers = [number for number in numbers if number < 0]
print(negative_numbers)

#Exercise 14 
two_or_more_numerals = [number for number in numbers if len(str(abs(number))) >= 2]
print(two_or_more_numerals)

#Exercise 15
numbers_squared = [number**2 for number in numbers]
print(numbers_squared)

#Exercise 16 
odd_negative_numbers = [number for number in numbers if number < 0 and number%2 != 0]
print(odd_negative_numbers)

#Exercise 17 
numbers_plus_five = [number + 5 for number in numbers]
print(numbers_plus_five)

#BONUS
def is_prime(n):
    if n > 1 and n != 2: 
        for i in range(2, n):
            if n % i == 0:
                return False 
            else: 
                return True 
    elif n == 2:
            return True

primes = [n for n in numbers if is_prime(n) == True]
print(primes)
