from os import system
from random import randint
import time
import msvcrt

import Levenshtein

file = open("nouns.txt")
word_container = [];

for words in file:
    word_container.append(words.strip())

file.close()

file = open("adjectives.txt")

for words in file:
    word_container.append(words.strip())

file.close()

while(True):
    system('cls')
    word_count = int(input("Enter the number of words you want to generate: "))
    system('cls')

    generated_words = ""

    for i in range(word_count):
        generated_words += word_container[randint(0, len(word_container))] + " "


    def instruction():
        max_dashes = 100
        dash = ""
        if len(generated_words) < max_dashes:
            for i in range(len(generated_words)):
                dash += "-"
        else:
            for i in range(max_dashes):
                dash += "-"

        print("\nType these generated words as fast as you can!\n" + dash + "\n" + generated_words + "\n" + dash)



    cooldown = 3

    for seconds in range(cooldown):
        instruction()

        print(str(cooldown) + "...")
        cooldown -= 1
        time.sleep(1)
        
        while msvcrt.kbhit():
            flush = input()

        system('cls')

    print("Go!")
    time.sleep(0.5)
    
    while msvcrt.kbhit():
        flush = input()
    
    system('cls')

    instruction()

    time_start = time.time()
    user_input = input()
    time_end = time.time()

    _time = str(round((time_end - time_start), 2))

    tpw = round((float(_time) / word_count), 2)
    tpl = round((float(_time) / (len(generated_words) - word_count)), 2)
    accuracy = round((((len(generated_words) - word_count) - (Levenshtein.distance(user_input, generated_words) - 1)) / (len(generated_words) - word_count)), 2)

    print("\nNumber of words: " + str(word_count))
    print("Number of letters: " + str(len(generated_words) - word_count))
    print("Time: " + _time + "s")
    print("Time / Word: " + str(tpw) + "s")
    print("Time / Letter: " + str(tpl) + "s")
    print("Accuracy: " + str(accuracy * 100) + "%")

    def rating_message(rating):
        random_message = [
            ["Don't give up!", "Type and type and type.", "You can do it!"],
            ["You're getting there!", "Don't stop practicing.", "Keep up the good work."],
            ["Nice!", "Good job!", "Keep it up!"],
            ["Impressive!", "Wow that's fast!", "Very good!"],
            ["You're a living computer!", "You are the Usain Bolt of typing!", "MARVELOUS!"]
        ]
        stars = ""
        for i in range(rating):
            stars += "*"

        return print("Your got (" + stars + ")" + " star" + ("s" if len(stars) > 1 else "") + ", " + random_message[rating-1][randint(0, 2)])

    def get_rating():
        if tpw <= 1 and (accuracy * 100) == 100:
            rating_message(5)
        elif tpw <= 3 and tpw > 1 and (accuracy * 100) == 100:
            rating_message(4)
        elif ((tpw <= 5 and tpw > 3) or (tpw <= 3 and tpw > 1)) and (accuracy * 100) > 90:
            rating_message(3)
        elif ((tpw <= 10 and tpw > 5) or ((tpw <= 5 and tpw > 3) or (tpw <= 3 and tpw > 1))) and (accuracy * 100) >= 75:
            rating_message(2)
        else:
            rating_message(1)
    
    get_rating()
    
    if str(input("\n\nDo you want to take the test again? (Input any key) (N - Stop): ")) == 'N':
        break