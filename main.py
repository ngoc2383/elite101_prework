# Collect user name
def my_name():
    name = input("What is your name? ")
    return name

# Collect user age and respond with welcome message
def my_age(name):
    age = None

    while age is None:
        try:
            age = int(input(f"Hello {name}, how old are you? "))
            if age < 0:
                print("Age cannot be negative.")
                age = None
        except (TypeError, ValueError):
            print("Your age must be a non-negative number!")
    
    if age < 15:
        print("Welcome young user!")
    elif age < 18:
        print("Welcome! How nice it is to be a teenager!")
    elif age < 55:
        print("Welcome! How's adulthood?")
    elif age < 120:
        print("Welcome! Did you retire yet?")
    else:
        print("Welcome! Are you on your way to break the world record for age?")

# Greets the user and call my_name and my_age function
def greeting():
    print("Welcome to the Museum Chatbot!")
    name = my_name()
    my_age(name)

# Ask how 
def help_menu():
    print("\nHow can I help you?\nPlease select from the options below:")
    print("1. What's the opening and closing time of the museum?")
    print("2. What's our museum about?")
    print("3. What should you bring when visiting our museum?")
    print("4. What's the recommended time to visit our museum?")
    print("5. Exit conversation")
    print("")

    
    choice = None
    while choice is None:
        try:
            choice = int(input("Enter the number of your choice: "))    
            if choice < 1 or choice > 5:
                print("Not a valid choice!")
                choice = None
        except (TypeError, ValueError):
            print("Input must be a number!")
            choice = None

    print("")
        

    if choice == 1:
        print("Our museum open at 8am and closes at 9pm everyday. For holiday, please check the annuoncement page for specific time. Hope this helps!")
    elif choice == 2:
        print("Our museum features epic coding and robotics projects from all over the world! You can find out more sbout this on our features page. Hope this helps!")
    elif choice == 3:
        print("We recommend you to bring your best camera to take pictures of your epic collections. Additionally, we recommend bringing your computer as we frequently have fun laps on robotics for our visitors. Hope this helps!")
    elif choice == 4:
        print("This depends on your freetime as well as preferences. Though weekends and holidays would be the best time to visit our museum as we have more fun labs for our visitors to participate. Hope this helps!")
    else:
        print("Thank you for your interest in our museum\nHave a good day!")

    if choice != 5:
        print("")
        reset_or_no = None
        while reset_or_no is None:
            reset_or_no = input("Would you like to ask another question?(y or n) ")
            if reset_or_no == "y":
                help_menu()
            elif reset_or_no == "n":
                print("Thank you for your interest in our museum\nHave a good day!")
            else:
                print("Invalid input.")
                reset_or_no = None


# Call functions ====================================================================================================================================================================================
greeting()
help_menu()