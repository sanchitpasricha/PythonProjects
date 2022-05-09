import art
import functions

print(art.logo)


while True:
    choice = input("What would you like? (espresso/latte/cappuccino) : ")
    if choice == 'report':
        functions.reportPrint()
        continue
    print("Please insert coins.")
    totalMoney = functions.moneyInput()
    functions.order(choice, totalMoney)
