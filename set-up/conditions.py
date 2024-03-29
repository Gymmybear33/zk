# trip_type = input("what type of trip are you taking?: ").lower()
# cost = int(input("Expected trip cost?: "))

# discount = trip_type == "business" and cost >= 1200

# print("Customer receives a discount:", discount)


# discount_code = input("Enter discount code ").lower()
# price = 150
# discount_price = price * .8

# if discount_code != "winter23":
#     print("The code is not valid")
# else:
#     print("your total is $", discount_price,
#           "...you saved: $", price * .2)


trip_cost = int(input("Trip Cost?: "))
bye = "Have fun!"

if trip_cost < 300:
    print("Go to a stay-cation", bye)
elif trip_cost >= 300 and trip_cost < 1000:
    print("Go to a road trip", bye)
elif trip_cost >= 1000:
    print("Catch a flight to the beach", bye)
