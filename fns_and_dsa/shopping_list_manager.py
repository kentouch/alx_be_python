# creating a shopping list where the user is prompt to choose to add an item in # an empty list or remove an item or view the list of the item.



def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View your list of items")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        # display first the menu
        display_menu()
        # Prompt the user to select the choosen option from the menu
        option = input("Enter your choice: ")
        # if choice is 1 meaning 'add item' 
        if option == "1" :
            # enter the item in the list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        # prompt the user if he selected 2 as a choice to enter an item from the list to remove
        elif option == "2":
            item = input("Enter the item to remove: ")
            if item not in shopping_list:
                print(f"The {item} do not exist in the list")
            else:
                shopping_list.remove(item)
        # prompt the user if he selected 3 to display the list of items
        elif option == "3":
             print(shopping_list)
        # prompt the user if he selected 4 to exit 
        elif option == "4":
            break
        else:
            print("Invalid input bro")

if __name__ == "__main__":
    main()
