watch_movie = input("Do you want to watch a movie? ").lower()

if watch_movie == "yes":
    genre = input("What genre you want to watch? ").lower()
    if genre == "comedy":
        print("Watch the Hangover Trilogy")
    else:
        print("Watch Top Gun")
else:
    print("Watch a TV series")

# --------------------------------------#

location = input("Hotel or Resort? ").lower()
if location == "resort":
    max_price = int(input("max price per night? "))
    if max_price >= 350:
        print("Book at Six Senses Resort")
    else:
        print("Go to the Four Seasons")
else:
    print("Go to the nearest Hilton")

# --------------------------------------#

product1 = int(input("Enter price for Product1 "))
product2 = int(input("Enter price for Product2 "))
product3 = int(input("Enter price for Product3 "))

if product3 >= product1 and product3 >= product2:
    print("The total cost for", product3, "is:", product1 * .5)
if product1 >= product2 and product1 >= product3:
    print("The total cost for", product1, "is:", product1 * .66)
