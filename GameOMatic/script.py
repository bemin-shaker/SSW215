
def start_game():

    char_dict = {}

    def init_inventory():
        inv_dict = {}
        name = input("\nWhat is this item called? (Leave blank to exit): ")
        while(name):
            num = int(input("Enter the number of this item: "))
            inv_dict[name] = num
            name = input("\nWhat is this item called? (Leave blank to exit): ")
        return inv_dict

    def add_char_copy():
        name = input(
            "\nEnter the name of your character, leave blank to exit: ")
        while(name):
            print_chars()
            copy = input('\nWhich character to copy inventory from?: ')
            if(copy in char_dict):
                char_dict[name] = char_dict[copy]
                print(name + ' created with same inventory as ' + copy)
            else:
                print("Character not recognized...")
            name = input(
                "\nEnter the name of your character(s) (leave blank to exit): ")

    def add_character():
        name = input(
            "\nEnter the name of your character (leave blank to exit): ")
        while(name):
            inventory = init_inventory()
            char_dict[name] = inventory
            name = input(
                "\nEnter the name of your character (leave blank to exit): ")

    def print_items(name):
        print("\nItems in " + name + "'s inventory: ")
        for item in char_dict[name]:
            print(item + ' - ' + str(char_dict[name][item]))

    def print_chars():
        print("\nCharacters in this game: ")
        for name in char_dict.keys():
            print(name)

    def modify_inv(type):

        def inv_empty(name, item):
            return char_dict[name][item] == 0

        def dec_item(name, item):
            if(not inv_empty(name, item)):
                char_dict[name][item] -= 1
                if inv_empty(name, item):
                    print(name + " now has " +
                          str(char_dict[name][item]) + " of that item...")
            else:
                print(name + " has no more of that item, can't decrement...")

        def inc_item(name, item):
            char_dict[name][item] += 1

        def remove_item(name, item):
            char_dict[name].pop(item)
            print(item + " removed from " + name + "'s inventory...")

        def add_item(name):
            item = input('What is the name of this item?: ')
            quant = int(input('How many of this item?: '))
            char_dict[name][item] = quant
            print(item + " added to " + name + "'s inventory...")

        print_chars()
        name = input(
            "Which character would you like to change the inventory of? (Leave blank to exit): ")
        if name in char_dict.keys():
            print_items(name)
            if type != 'add':
                item = input('Which item to modify?: ')
                if item in char_dict[name]:
                    if type == 'dec':
                        dec_item(name, item)
                    if type == 'inc':
                        inc_item(name, item)
                    if type == 'rem':
                        remove_item(name, item)
                else:
                    print("That item is not in " +
                          name + "'s inventory...")
            else:
                add_item(name)
        else:
            print("Character not recognized...")

    # main loop of the program
    while(1):
        print('\n1 to add new character with unique inventory')
        print('2 to make new character with copy of inventory')
        print('3 to decrement character inventory')
        print('4 to increment character inventory')
        print('5 to add an item to a character')
        print('6 to remove an item from a character')
        response = input('What would you like to do? Leave blank to exit: ')
        if(response):
            if response == '1':
                add_character()
            if response == '2':
                add_char_copy()
            if response == '3':
                modify_inv('dec')
            if response == '4':
                modify_inv('inc')
            if response == '5':
                modify_inv('add')
            if response == '6':
                modify_inv('rem')
        else:
            print('Exiting game...')
            break


def test():
    from random import randint
    from collections import Counter
    results = []
    for _ in range(10000):
        results += [randint(1, 12)]
    print(Counter(results))


if __name__ == '__main__':
    while(1):
        print('\nPress 1 to test')
        print('Press 2 to start game')
        result = input('To exit leave blank: ')
        if result == '1':
            test()
        elif result == '2':
            start_game()
        else:
            print('Exiting GameOMatic...')
            break
