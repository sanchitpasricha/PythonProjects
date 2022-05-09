import resources


money = {
    'quarters': 0,
    'dimes': 0,
    'nickles': 0,
    'pennies': 0,
}

def resourceCheck(typeC):
    if resources.MENU[typeC]["ingredients"]["water"] > resources.resources['water']:
        return False
    if resources.MENU[typeC]["ingredients"]['milk'] > resources.resources['milk']:
        return False
    if resources.MENU[typeC]["ingredients"]['coffee'] > resources.resources['coffee']:
        return False
    else:
        return True

def moneyInput():
    money['quarters'] = int(input("How many quarters :: "))
    money['dimes'] = int(input("How many dimes :: "))
    money['nickles'] = int(input("How many nickles :: "))
    money['pennies'] = int(input("How many pennies :: "))
    total = money['quarters'] * 0.25 + money['dimes'] * 0.1 + money['nickles'] * 0.05 + money['pennies'] * 0.01
    return total

def reportPrint():
    print(f"Water: {resources.resources['water']}ml\nMilk: {resources.resources['milk']}ml\n"
          f"Coffee: {resources.resources['coffee']}ml\nMoney: ${resources.resources['money']}\n")

def updateDispenser(drink):
    resources.resources['water'] -= resources.MENU[drink]['ingredients']['water']
    resources.resources['milk'] -= resources.MENU[drink]['ingredients']['milk']
    resources.resources['coffee'] -= resources.MENU[drink]['ingredients']['coffee']
    resources.resources['money'] += resources.MENU[drink]['cost']

def display(drink, paid):
    if paid < resources.MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return

    change = paid - resources.MENU[drink]['cost']
    print(f"Here is ${change} in change.")
    print(f"Here is your {drink} ☕️. Enjoy!")
    updateDispenser(drink)

def order(drinktype, paid):
    if not resourceCheck(drinktype):
        print("Dispenser out of resources!")
        return

    display(drinktype, paid)
