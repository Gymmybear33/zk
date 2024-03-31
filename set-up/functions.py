# def user(name, age, nationality):
#     print("Hello,", name)
#     print("You are", age, "years old")
#     print("You are", nationality)


# number_of_users = int(input("How many users do you want? "))
# for i in range(number_of_users):
#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     nationality = input("What is your nationality? ")
#     user(name, age, nationality)

# ----------------------------------------#

# def good_deal(cost):
#     if cost >= 50 and cost < 150:
#         response = "This is a good deal!"
#     elif cost > 150:
#         response = "Overpriced!"
#     else:
#         response = "Cheap, Buy Now!"
#     return response


# store = input("Enter Store Name: ")
# cost = float(input("Item Cost: "))
# res = good_deal(cost)
# print(store, "-", res)
# if res == "This is a good deal!":
#     print("Buy before it's too late")

# ----------------------------------------#

# def class_scores(grade):
#     if grade > 0 and grade < 50:
#         print("Below passing, improve your grade.")
#     elif grade >= 50 and grade < 70:
#         print("Barely passing the class")
#     elif grade >= 70 and grade < 90:
#         print("Yoh have a passing grade")
#     else:
#         print("You are one of the best in the class!")


# for i in range(4):
#     grade = float(input("What was your score? "))
#     print(class_scores(grade))


# ----------------------------------------#

# def flight_charges():
#     for i in range(2):
#         base_fare = 500
#         upgrade = input("Do you want to upgrade? ").lower()
#         baggage = input("Will you have a baggage? ").lower()
#         tax = .08
#         if upgrade == "yes" and baggage == "yes":
#             sub_total = (base_fare + 99 + 35)
#             total = sub_total + (sub_total * .08)
#             print(total)
#         elif upgrade == "yes" and baggage == "no":
#             sub_total = base_fare + 99
#             total = sub_total + (sub_total * .08)
#             print(total)
#         elif baggage == "yes" and upgrade == "no":
#             sub_total = base_fare + 35
#             total = sub_total + (sub_total * .08)
#             print(total)
#         else:
#             total = base_fare + (base_fare * .08)
#             print("Your total is:", total)


# flight_charges()

# ----------------------------------------#

# def terminal_1():
#     print("Departing from terminal 1 - Budget")
#     flight_check()


# def terminal_2():
#     print("Departing from terminal 2 - domestic")
#     flight_check()


# def terminal_3():
#     print("Departing from terminal 3 - International")
#     flight_check()


# def flight_check():
#     answer = input("Budget/Domestic or International: ").lower()

#     if answer == "budget":
#         terminal_1()
#     elif answer == "domestic":
#         terminal_2()
#     elif answer == "international":
#         terminal_3()
#     else:
#         print("I couldn't find that terminal.")


# flight_check()


# ----------------------------------------#


def calculate_bmi(weight, height):
    calculation = weight / (height * height)
    return calculation


def show_results(weight, height):
    calculate = calculate_bmi(weight, height)
    if calculate <= 18.5:
        print("You are considered underweight")
    elif calculate > 18.5 and calculate <= 25:
        print("Your BMI is considered normal")
    else:
        print("You are considered overweight")


people = int(input("Enter number of people: "))
for i in range(people):
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    show_results(weight, height)
