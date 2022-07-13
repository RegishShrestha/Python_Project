MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


total = 0
user_input = ''


def check(user_input):
    user_drink = ''
    if user_input == 'espresso':
        user_drink = MENU['espresso']
        return user_drink
    elif user_input == 'latte':
        user_drink = MENU['latte']
        return user_drink
    elif user_input == 'cappuccino':
        user_drink = MENU['cappuccino']
        return user_drink
    elif user_input == 'report':
        print(resources)
    elif user_input == 'off':
        print("Turning off")


def getan(user_input, user_drink,):
    global total
    if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        print(user_drink)
        user_cost = user_drink['cost']
        print(user_cost)
        # //drinks total VALID_MODULE_NAME
        drink_water = user_drink['ingredients']['water']
        if user_input == 'espresso':
            drink_milk = 0
        else:
            drink_milk = user_drink['ingredients']['milk']
        drink_coffee = user_drink['ingredients']['coffee']

        # checking resourses
        if resources['water'] >= drink_water and resources['milk'] >= drink_milk and resources['coffee'] >= drink_coffee:
            # //cash total
            quarters = int(input('how many quarters: '))
            dimes = int(input('how much dimes: '))
            nickles = int(input('how much nickles: '))
            pennies = int(input('how much pennies: '))
            total_coin = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01

            if total_coin == user_cost:
                print(f'Here is your {user_input} ☕️. Enjoy!')
                resources['water'] -= drink_water
                resources['milk'] -= drink_milk
                resources['coffee'] -= drink_coffee
                total += user_cost

            elif total_coin > user_cost:
                print(f'Here is your {user_input} ☕️. Enjoy!')
                print(f'Here is ${round(total_coin-user_cost,2)} in change.')
                resources['water'] -= drink_water
                resources['milk'] -= drink_milk
                resources['coffee'] -= drink_coffee
                total += user_cost
            elif total_coin < user_cost:
                print("Sorry not enough coin")
        else:
            print("Sorry not enough resourses")


while user_input != 'off':
    # TODO take input from user
    print(MENU)
    user_input = input(
        "What would you like? (espresso/latte/cappuccino):").lower()

    # TODO to check the input from user
    user_drink = check(user_input)

    # if user_input == 'espresso':
    #     user_drink = MENU['espresso']
    # elif user_input == 'latte':
    #     user_drink = MENU['latte']
    # elif user_input == 'cappuccino':
    #     user_drink = MENU['cappuccino']
    # elif user_input == 'report':
    #     print(resources)
    # elif user_input == 'off':
    #     print("Turning off")

    # TODO to calculate all things
    getan(user_input, user_drink)
    # if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
    #     print(user_drink)
    #     user_cost = user_drink['cost']
    #     print(user_cost)
    #     # //drinks total VALID_MODULE_NAME
    #     drink_water = user_drink['ingredients']['water']
    #     if user_input == 'espresso':
    #         drink_milk = 0
    #     else:
    #         drink_milk = user_drink['ingredients']['milk']
    #     drink_coffee = user_drink['ingredients']['coffee']

    #     # checking resourses
    #     if resources['water'] >= drink_water and resources['milk'] >= drink_milk and resources['coffee'] >= drink_coffee:
    #         # //cash total
    #         quarters = int(input('how many quarters: '))
    #         dimes = int(input('how much dimes: '))
    #         nickles = int(input('how much nickles: '))
    #         pennies = int(input('how much pennies: '))
    #         total_coin = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01

    #         if total_coin == user_cost:
    #             print(f'Here is your {user_input} ☕️. Enjoy!')
    #             resources['water'] -= drink_water
    #             resources['milk'] -= drink_milk
    #             resources['coffee'] -= drink_coffee
    #             total += user_cost

    #         elif total_coin > user_cost:
    #             print(f'Here is your {user_input} ☕️. Enjoy!')
    #             print(f'Here is ${total_coin-user_cost} in change.')
    #             resources['water'] -= drink_water
    #             resources['milk'] -= drink_milk
    #             resources['coffee'] -= drink_coffee
    #             total += user_cost
    #         elif total_coin < user_cost:
    #             print("Sorry not enough coin")
    #     else:
    #         print("Sorry not enough resourses")
    print(f'TOtal cash earned= {total}')
    print(f'total resourses={resources}')
print(f'TOtal cash earned= {total}')
print(f'total resourses={resources}')
