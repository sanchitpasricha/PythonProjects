import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen = random.choice(hangman_words.word_list)
print("Random name generated!")
answer = []
for i in range(len(chosen)):
    answer += "_"
print(answer)

end = False
chance = 6
while not end:
    letter = input("Enter an alphabet :: ")
    for i in range(0, len(answer)):
        if (chosen[i] == letter):
            answer[i] = letter

    if letter not in answer:
        chance -= 1
        print(hangman_art.stages[chance])

    print(answer)

    if (chance > 0):
        if "_" not in answer:
            end = True
            print("You Win!")
    else:
        end = True
        print(f"The word was :: {chosen}")
        print("You Lost!")