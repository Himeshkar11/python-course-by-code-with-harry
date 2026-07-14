import datetime

def get_time():
    return datetime.datetime.now()

print("welcome to himesh fitness camp")
# person_name = int(input("what is your name? \n choose 1 for harry \n choose 2 for rohan\n choose 3 for hammad "))
# if person_name == 1:
#     print("welcome harry what do you want to access\n enter 1 for food and \n enter 2 for exercise")
#     type_fitness = int(input())
#     if type_fitness == 1:
#         type_of_food = input("Enter the food you ate")
#         f = open("harry-food.txt","w")
#         f.write(f"{get_time()}, ate{type_of_food} ")
#         f.close()
#     if type_fitness == 2:
#         type_of_exercise = input("Enter the exercise you did")
#
#         f = open("harry-exercise.txt","w")
#         f.write(f"{get_time()}, did {type_of_exercise} ")
#         f.close()
# if person_name == 2:
#     print("welcome Rohan what do you want to access\n enter 1 for food and \n enter 2 for exercise")
#     type_fitness = int(input())
#     if type_fitness == 1:
#         type_of_food = input("Enter the food you ate")
#         f = open("rohan-food.txt", "w")
#         f.write(f"{get_time()}, ate{type_of_food} ")
#         f.close()
#     if type_fitness == 2:
#         type_of_exercise = input("Enter the exercise you did")
#
#         f = open("rohan-exercise.txt", "w")
#         f.write(f"{get_time()}, did {type_of_exercise} ")
#         f.close()
# if person_name == 3:
#     print("Welcome Hammad what do you want to access \n enter 1 for food and \n enter 2 for exercise")
#     type_fitness = int(input())
#     if type_fitness == 1:
#         type_of_food = input("Enter the food you ate")
#         f = open("hammad-food.txt", "w")
#         f.write(f"{get_time()}, ate{type_of_food} ")
#         f.close()
#     if type_fitness == 2:
#         type_of_exercise = input("Enter the exercise you did")
#
#         f = open("hammad-exercise.txt", "w")
#         f.write(f"{get_time()}, did {type_of_exercise} ")
#         f.close()

def function_fitness(person_name):
    print(f"Welcome {person_name} what do you want to access \n enter 1 for food and \n enter 2 for exercise")
    type_fitness = int(input())
    if type_fitness == 1:
        type_of_food = input("Enter the food you ate")
        f = open(f"{person_name}-food.txt", "a")
        f.write(f"\n {get_time()}, ate{type_of_food} ")
        f.close()
    if type_fitness == 2:
        type_of_exercise = input("Enter the exercise")
        f = open(f"{person_name}-exercise.txt", "a")
        f.write(f"\n {get_time()}, did {type_of_exercise} ")
        f.close()
person_name = input("Enter the person name")
function_fitness(person_name)

