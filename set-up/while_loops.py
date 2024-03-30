# password = input("Enter password: ")

# while password != "rambo123":
#     print("Incorrect Password")
#     password = input("Try again: ")
# print("Welcome to your account!")

# ------------------------------------#

# cost = int(input("Enter the cost of an item(0 to end): "))
# total = 0

# while cost != 0:
#     total += cost
#     cost = int(input("Enter the cost of an item (0 to end): "))
# print("Grand Total:", total)
# total = total * .5
# print("Total price with discount:", total)

# ------------------------------------#

# test_answer = input("Enter a, b, c, or d: ")
# num_tries = 1
# while test_answer != "c":
#     num_tries += 1
#     print("Wrong answer!")
#     test_answer = input("Try again: ")

# print("It took you", num_tries, "tries to get the answer.")

# ------------------------------------#

# message = input("Send a message: ").lower()
# while message != "done":
#     print("We got your message!")
#     message = input("Send a message: ").lower()

# ------------------------------------#

# password = input("Enter your password: ")
# while password != "hola" and password != "jayson":
#     password = input("Let's try again! ")
# print("Welcome to your account!")

# ------------------------------------#

# name = input("Enter name: ").capitalize()
# num_bookings = 0
# while num_bookings < 3 and name != 'Done':
#     num_bookings += 1
#     print("Congrats", name, "You've saved 20%")
#     name = input("Enter name: ").capitalize()
#     while num_bookings >= 3 and name != "Done":
#         print("Sorry,", name, "!", "no more discounts...")
#         name = input("Enter name: ").capitalize()

# ------------------------------------#

language = input("Enter a Programming Language: ").capitalize()
counter = 1
while counter < 5 and language != "Python":
    counter += 1
    language = input("Try another langauge!: ").capitalize()

if counter == 1:
    print("It took you", counter, "try to say Python")
elif language == "Python":
    print("It took you", counter, "tries to say Python")
else:
    print("sorry, you didn't say Python")
