import art
import random
import decision

print(art.logo)

flag = True

while flag:

    cardList = ['11', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
    finalSum_user = 0
    finalSum_cmp = 0

    leaderBoard = {
        'userList': [],
        'cmpList': [],
    }

    choice = input("Do you want to play a game of blackjack ? Type 'y' or 'n' ").lower()
    # let's start the game

    if choice == 'y':
        leaderBoard['userList'] += random.sample(cardList, 2)
        for card in leaderBoard['userList']:
            finalSum_user += int(card)
        print(f"Your cards: {leaderBoard['userList']}, Current Score: {finalSum_user}")

        leaderBoard['cmpList'] += random.sample(cardList, 2)
        for card in leaderBoard['cmpList']:
            finalSum_cmp += int(card)
        print(f"Computer's first card: {leaderBoard['cmpList'][0]}")

        choice2 = input("Type 'y' to get another card else 'n' to pass. ").lower()

        if choice2 == 'y':
            leaderBoard['userList'] += random.sample(cardList, 1)
            finalSum_user += int(leaderBoard['userList'][2])

        if finalSum_cmp < 21:
            leaderBoard['cmpList'] += random.sample(cardList, 1)
            finalSum_cmp += int(leaderBoard['cmpList'][2])

        print(f"Your final hand: {leaderBoard['userList']}, final score: {finalSum_user}")
        print(f"Computer's final hand: {leaderBoard['cmpList']}, final score: {finalSum_cmp}")
        statement = decision.compare(user_score=finalSum_user, computer_score=finalSum_cmp)
        print(statement)
    else:
        flag = False
