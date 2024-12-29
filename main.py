def my_name():
    name = input("What is your name? ")
    return name

def my_age(name):
    try:
        age = int(input("Hello " + name + ", how old are you? "))
    except TypeError:
        my_age()
    
    if age < 15:
        print("Welcome young user!")
    elif age >= 15 and age < 18:
        print("Welcome! How nice it is to be a teenager!")
    elif age >= 18 and age < 55:
        print("Welcome! How's adulthood?")
    elif age >=55 and age < 120:
        print("Welcome! Did you retired yet?")
    elif age >= 120:
        print("Welcome! Are you on your way to break the world record for age?")

def greeting():
    print("Welcome to the Museum Chatbot!")
    name = my_name()
    my_age(name)

def help_menu():
    print("\nHow can I help you?\nPlease select from the options below:")
    print("1. What's the opening and closing time of the museum?")
    print("2. What's our museum about?")
    print("3. What should you bring when visiting our museum?")
    print("4. ")
    




# Call functions ====================================================================================================================================================================================
greeting()
help_menu()