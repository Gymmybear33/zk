# username = input("Enter username: ")
# invalid = "!@#$%"

# for letter in username:
#     print(letter)
#     if letter in invalid:
#         print("This character is not allowed:", letter)


# -------------------------------------------#


# for i in range(5):
#     number = int(input("Enter a number: "))
#     print("Number added!,", number)
# print("All 5 numbers have been added!")


# -------------------------------------------#

# passengers = int(input("How many passengers? "))
# for i in range(passengers):
#     last_name = input("Enter last name: ").capitalize()
#     print("Hello", last_name)
# print("Passenger Manifest Updated!")


# -------------------------------------------#

# password = input("Password: ")
# invalid = "!@#$%*()"
# for i in password:
#     if i in invalid:
#         print("This is an invalid character", i)


# -------------------------------------------#


# word = input("Enter a word: ")
# vowels = "aeiou"
# counter = 0
# for i in word:
#     if i in vowels:
#         counter += 1
# print("There is:", counter, "vowels in in:", word)

# -------------------------------------------#

# number = input("Enter a phone number: ")
# valid = "0123456789+"
# for i in number:
#     if i not in valid:
#         print("Invalid number!")
#         break

# -------------------------------------------#

# guests = int(input("How many guests?: "))
# for i in range(guests):
#     name = input("What's your name?: ")
#     age = int(input("What's your age?:"))
#     if age > 18:
#         print("Welcome", name)
#     else:
#         print("Must be 18 to drink!")

# -------------------------------------------#

for i in range(5):
    username = input("Username: ").lower()
    password = input("Password: ")
    if username == "admin" and password == "12345":
        print("Welcome Admin")
        break
if username != "admin" and password != "12345":
    print("Yoy are not the admin")
