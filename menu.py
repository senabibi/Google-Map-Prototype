
def display_menu():
    print("\nMenu:")
    print("a. Enter city")
    print("b. Print current city")
    print("c. List k closest cities")
    print("d. Find shortest path to")
    print("x. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def get_city_name():
    return input("Enter city name: ")

def get_k_value():
    return int(input("Enter the value of k: "))

def get_destination_city():
    return input("Enter destination city: ")

def display_invalid_choice():
    print("Invalid choice. Please try again.")
