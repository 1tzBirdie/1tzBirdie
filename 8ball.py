#this is a code for magic 8ball... just ask a question, and get ready to be surprised!


import sys
import random

ans1 = True

while ans1:
    que = input("Ask the magic 8 ball a question(1-8) press .(dot) if you want to exit ")
    print("\n")

    ans = random.randint(1, 20)

    if que == ".":
        sys.exit()

    elif ans == 1:
        print("It is certain")

    elif ans == 2:
        print("It is decidedly so.")

    elif ans == 3:
        print("You may rely on it")

    elif ans == 4:
        print("Without a doubt")

    elif ans == 5:
        print("Yes definitely.")

    elif ans == 6:
        print("As I see it, yes.")

    elif ans == 7:
        print("Most likely.")

    elif ans == 8:
        print("Outlook good.")

    elif ans == 9:
        print("Yes.")

    elif ans == 10:
        print("Signs point to yes.")

    elif ans == 11:
        print("Reply hazy, try again.")

    elif ans == 12:
        print("Ask again later.")

    elif ans == 13:
        print("Better not tell u rn.")

    elif ans == 14:
        print("Cannot predict now.")

    elif ans == 15:
        print("Concentrate and ask again man, you arent concentrating enough")

    elif ans == 16:
        print("Don't count on it")

    elif ans == 17:
        print("My reply is no.")

    elif ans == 18:
        print("My sources say no.")

    elif ans == 19:
        print("Outlook not so good.")

    elif ans == 20:
        print("Very doubtful")