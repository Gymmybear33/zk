enter = input("Enter 1 - To Start -or- Enter 2 - To Stop")
pr_firstclass = 1000
pr_businessclass = 500
sd_firstclass = 2000
sd_businessclass = 1000
ny_firstclass = 800
ny_businessclass = 400
ny_train = 500

while enter != "2":
    for i in range(2):
        destination = input(
            "Do you have some place in mind for your next trip? ").lower()
        if destination == "yes":
            where = input(
                "Wonderful, where? ... We only offer trips to PUERTO RICO, SANTO DOMINGO or NEW YORK! ").upper()
            if where == "NEW YORK":
                transport = input(
                    "Awesome, are you.... FLYING, DRIVING or taking the TRAIN?").upper()
                if transport == "FLYING":
                    seat_class = input(
                        "Would you prefer: FIRST or BUSINESS class?").upper()
                    if seat_class == "FIRST":
                        print("First class tickets costs are:",
                              ny_firstclass, "per passenger.")
                        passengers = int(input(
                            "How many people would go in this trip? "))
                        total = ny_firstclass * passengers
                        print(
                            "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)
                    else:
                        print("Business class tickets for New York are:",
                              ny_businessclass, "per passenger")
                    passengers = int(
                        input("How many people would be in this trip? "))
                    total = ny_businessclass * passengers
                    print(
                        "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)
                if transport == "TRAIN":
                    print("Train tickets for New York costs are:",
                          ny_train, "per passenger.")
                    passengers = int(input(
                        "How many people would go in this trip? "))
                    total = ny_train * passengers
                    print(
                        "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)
            elif where == "PUERTO RICO":
                seat_class = input(
                    "Well, I guess we are flying... would you like FIRST or BUSINESS class?").upper()
                if seat_class == "FIRST":
                    print("First class tickets for Puerto Rico are:",
                          pr_firstclass, "per passenger")
                    passengers = int(
                        input("How many people would be in this trip? "))
                    total = pr_firstclass * passengers
                    print(
                        "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)
                else:
                    print("Business class tickets for Puerto Rico are:",
                          pr_businessclass, "per passenger")
                    passengers = int(
                        input("How many people would be in this trip? "))
                    total = pr_businessclass * passengers
                    print(
                        "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)
            elif where == "SANTO DOMINGO":
                seat_class = input(
                    "Well, I guess we are flying... would you like FIRST or BUSINESS class?").upper()
                if seat_class == "FIRST":
                    print("First class tickets for Santo Domingo are:",
                          sd_firstclass, "per passenger")
                    passengers = int(
                        input("How many people would be in this trip? "))
                    total = pr_firstclass * passengers
                    print(
                        "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)
                else:
                    print("Business class tickets for Santo Domingo are:",
                          pr_businessclass, "per passenger")
                    passengers = int(
                        input("How many people would be in this trip? "))
                    total = pr_businessclass * passengers
                    print(
                        "Thank you for trusting us with your travel booking. Your total cost for this trip is:", total)

        elif destination == 'no':
            trip_type = input(
                "I can help you with that... would you prefer BEACH, CITY or MOUNTAINS?").upper()
            if trip_type == "BEACH" or trip_type == "MOUNTAINS":
                pr = input(
                    "How about Puerto Rico? Would that interest you?").lower()
                if pr == "yes":
                    print("That's awesome, I'll get start working on that")
                elif pr != "yes":
                    sd = input(
                        "Ok, we stil have plenty of options... how about Santo Domingo?").lower()
                    if sd == "yes":
                        print("Weee... that's great news! I'm your guy!")
                    else:
                        print("So sorry, those two were my only options.")
            elif trip_type == "CITY":
                ny = input("How about New York?")
                if ny == "yes":
                    print("Wow, we are on a roll here! I'll start the paperwork")
                else:
                    print("So sorry I wasn't much of a help. Maybe next time.")
