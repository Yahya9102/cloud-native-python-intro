from users import add_user, list_users, user_exists

# TODO 
# ADD Delete to menu
# Add update to menu


def show_menu():
    print("\n---User console---")
    print("1) Add user")
    print("2) List users")
    print("3) Search for user")
    print("4) Exit")



# TODO 
# ADD Delete handler
# Add update handler


def handle_add_user():
    name = input("Enter your username: ")
    success = add_user(name)

    if success:
        print(f"user {name.strip()} saved")
    else: 
        print("""could not save user
              name may already be in use or empty""")

def handle_list_users():
    all_users = list_users()
    if len(all_users) == 0:
        print("there are no users yet")
    else:
        print("\n registered users")
        for i, name in enumerate(all_users, start=1):
            print(f"{i}, {name}")    
        




def handle_search_user():
    name = input("Enter username to search for: ")
    if user_exists(name):
        print(f"Yes, user {name.strip()} exists")
    else:
        print(f"No, user {name.strip()} does not exist")



def main():

    while True:
        show_menu()

        choice = input("chose an option(1-4)")
        if choice == "1":
            handle_add_user()
        elif choice == "2":
            handle_list_users()
        elif choice == "3":
            handle_search_user()
        elif choice == "4":
            print("Exiting program byee")
            break        
        else:
            print("invalid choice, try again")    


if __name__ == "__main__":
    main()



# name = input("What is your name? ")
# name = name.strip()

# print(f"Hello {name}")


# count = 0

# while count < 3:
#     print("count:", count)
#     count += 1


# for i in range(5):
#     print("Value", i)



# names = ["Yahya", "Elias", "Rebecca"]

# for name in names:
#     print(name)




#if-satser

# age = 20

# if age >= 18:
#     print("you are an adult")
# elif age >= 100:
#     print("you are too old")
# else:
#     print("you are too young")




#functions

#def add(a, b):
#    return a + b

#result = add(3,4)
#print(result)

#def greet_name(name): 
#    print("Hej", name)    
#greet_name("Yahya")





#dict
#person = {
#    "name": "Yahya",
#    "age": 34,
#    "is_teacher": True
#}


#Lists
#number = [1,2,3,4]
#names = ["Sara", "Yahya", "Thomas"]
#mixed = [1, "Yahya", True, 3.14]

#print(number, names, mixed)


# pythons null
#result = None




# boolean
#is_logged_in = True
#has_access = False

#print(is_logged_in, has_access)


#Float

#price  = 19.99
#negative_price = -33.3
#print(price,negative_price)


#integers
# amount = 10
# negative = -5
# big_number = 3214983290489328402394204

# print(big_number)


# Different type of string
#text = "Hello"
#text_two = 'Hello from enkelfnutt'
#long_text = """ det här är en sträng som kan 
#sträcka sig över 
#flera rader
#och fortfarande fungera
#"""


#print (long_text)
