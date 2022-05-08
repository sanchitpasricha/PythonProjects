import random
import data
import art

print(art.logo)

game = {
    "first": random.choice(data.data),
    "second": random.choice(data.data)
}

score = 0

flag = True

while flag:

    if game['first'] == game['second']:
        game['second'] = random.choice(data.data)

    print(f"Compare A: {game['first']['name']}, a {game['first']['description']}, from {game['first']['country']} ")
    print(art.vs)
    print(f"Against B: {game['second']['name']}, a {game['second']['description']}, from {game['second']['country']} ")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == 'a':
        if game['first']['follower_count'] > game['second']['follower_count']:
            score += 1
            game['first'] = game['second']
            game['second'] = random.choice(data.data)
        else:
            flag = False
    elif choice == 'b':
        if game['second']['follower_count'] > game['first']['follower_count']:
            score += 1
            game['first'] = game['second']
            game['second'] = random.choice(data.data)
        else:
            flag = False

print(f"Your Score is :: {score}")