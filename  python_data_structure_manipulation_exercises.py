students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

#1 
print(len(students))

#2 
light_coffee = len([student for student in students if student['coffee_preference'] == 'light'])
medium_coffee = len([student for student in students if student['coffee_preference'] == 'medium'])
dark_coffee = len([student for student in students if student['coffee_preference'] == 'dark'])

print(light_coffee, "students prefer light coffee.", medium_coffee, "students prefer medium coffee.", dark_coffee, "students prefer dark coffee.")

#3
pet_counts = {"dog": 0, "cat": 0, "horse": 0}
for student in students:
        for pet in student["pets"]:
            pet_counts[pet["species"]] += 1
print(pet_counts)

#4 
for student in students:
    print(len(student["grades"]))
##Yes every student has 4 grades

#5 
for student in students:
    grades = student["grades"]
    average_grade = (sum(grades))/(len(grades))
    print("This student's average grade is", average_grade)

#6 
for student in students:
    print(len(student["pets"]))

#7
web_development = len([student for student in students if student["course"] == "web development"])
data_science = len([student for student in students if student["course"] == "data science"])
print(web_development, "students are studying web development.", data_science, "students are studying data science.")

#8 
number_of_pets = []
for student in students:
    if student["course"] == "web development":
        number_of_pets.append(len(student["pets"]))
print(sum(number_of_pets)/len(number_of_pets))

#9
pet_age = []
for student in students:
    if student["course"] == "data science":
        for pet in student["pets"]:
            pet_age.append(pet["age"])
print(sum(pet_age)/len(pet_age))   

#10
coffee_count = {"dark": 0, "medium": 0, "light": 0}
for student in students: 
    if student["course"] == "data science":
        if student["coffee_preference"] == "dark":
            coffee_count["dark"] +=1
        if student["coffee_preference"] == "medium":
            coffee_count["medium"] +=1
        if student["coffee_preference"] == "light":
            coffee_count["light"] +=1
print("The most popular type of cofee among data science students is", max(coffee_count), "coffee.")

#11
coffee_count = {"dark": 0, "medium": 0, "light": 0}
for student in students: 
    if student["course"] == "web development":
        if student["coffee_preference"] == "dark":
            coffee_count["dark"] +=1
        if student["coffee_preference"] == "medium":
            coffee_count["medium"] +=1
        if student["coffee_preference"] == "light":
            coffee_count["light"] +=1
print("The least popular coffee type among web development students is", min(coffee_count), "coffee.")

#12
grades = []
for student in students:
    if len(student["pets"]) >= 2:
        for grade in student["grades"]:
            grades.append(grade)
print(sum(grades)/len(grades))

#13
student_with_three_pets = []
for student in students: 
    if len(student["pets"]) == 3:
        student_with_three_pets.append(student["student"]) 
print(len(student_with_three_pets))

#14
grades_of_students_with_no_pets = []
for student in students: 
    if len(student["pets"]) == 0:
        for grade in student["grades"]:
            grades_of_students_with_no_pets.append(grade)
print(sum(grades_of_students_with_no_pets)/len(grades_of_students_with_no_pets))

#15 
grades_web_development = []
grades_data_science = []
for student in students:
    if student["course"] == "data science":
        for grade1 in student["grades"]:
            grades_data_science.append(grade1)
    if student["course"] == "web development":
        for grade2 in student["grades"]:
            grades_web_development.append(grade2)
print("The average grade of data science students is ", sum(grades_data_science)/len(grades_data_science))
print("The average grade of web development student is", sum(grades_web_development)/len(grades_web_development))

#16 
grades_dark_coffee = []
for student in students:
    if student["coffee_preference"] == "dark":
        grades_dark_coffee.append(sum(student["grades"])/len(student["grades"]))
print(max(grades_dark_coffee) - min(grades_dark_coffee))

#17 
pets_medium_coffee = []
for student in students:
    if student["coffee_preference"] == "medium":
        pets_medium_coffee.append(len(student["pets"]))
print(sum(pets_medium_coffee)/len(pets_medium_coffee))

#18
pet_counts = {"dog": 0, "cat": 0, "horse": 0}
for student in students:
    if student["course"] == "web development":
         for pet in student["pets"]:
            pet_counts[pet["species"]] += 1
print(max(pet_counts))

#19 
student_names_length = []
for student in students:
    student_names_length.append(len(student["student"]))
print(sum(student_names_length)/len(student_names_length))

#20
pet_age_for_light_coffee_drinker = []
for student in students:
    if student["coffee_preference"] == "light":
        for pet in student["pets"]:
            pet_age_for_light_coffee_drinker.append(pet["age"])
print(max(pet_age_for_light_coffee_drinker))