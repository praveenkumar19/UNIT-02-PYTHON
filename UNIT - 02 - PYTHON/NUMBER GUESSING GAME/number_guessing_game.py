print("WELCOME TO NUMBER GUESSSING GAME")
print("IF YOU WANT TO PLAY A GAME WITH ME")
print("1 = YES ")
print("2 = NO ")
a=int(input("Enter your choice : "))
if a == 1:
    print("YES , LETS START THE GAME")
    print("CHOOSE A NUMBER BETWEEN 1 - 10")
    print("ARE YOU CHOOSE A NUMBER ?? ")
    print("1 = YES ")
    b=int(input("Enter your choice : "))
    if b == 1:
        print("IF THE NUMBER IS GREATER THAN 5 OR LESS THAN EQUAL TO 5")
        print("1 = GREATER THAN 5")
        print("2 = LESS THAN EQUAL TO 5")
        c=int(input("Enter your choice : "))
        if c == 1:
            print("IF THE NUMBER IS GREATER THAN 8 OR LESS THAN EQUAL TO 8")
            print("1 = GREATER THAN 8")
            print("2 = LESS THAN EQUAL TO 8")
            d=int(input("Enter your choice : "))
            if d == 1:
                print("YOUR NUMBER IS 9 ") 
                print("1 = CORRECT")
                print("2 = INCORRECT")
                ans=int(input("Enter your answer : "))
                if ans == 1:
                    print("CORRECT ANSWER")
                elif ans == 2:
                    print("INCORRECT ANSWER")
                    print("YOUR NUMBER IS 10 ")
                    print("CORRECT ANSWER")
            elif d == 2:
                print("YOUR NUMBER IS 6 ") 
                print("1 = CORRECT")
                print("2 = INCORRECT")
                ch=int(input("Enter your answer : "))
                if ch == 1:
                    print("CORRECT ANSWER")
                elif ch == 2:
                    print("INCORRECT ANSWER")
                    print("YOUR NUMBER IS 7 ")
                    print("1 = CORRECT")
                    print("2 = INCORRECT")
                    ns=int(input("Enter your answer : "))
                    if ns == 1:
                        print("CORRECT ANSWER")
                    elif ns == 2:
                        print("INCORRECT ANSWER")
                        print("YOUR NUMBER IS 8 ")
                        print("CORRECT ANSWER")
        elif c == 2:
            print("IF THE NUMBER IS GREATER THAN 3 OR LESS THAN EQUAL TO 3")
            print("1 = GREATER THAN 3")
            print("2 = LESS THAN EQUAL TO 3")
            d=int(input("Enter your choice : "))
            if d == 1:
                print("YOUR NUMBER IS 4 ")
                print("1 = CORRECT")
                print("2 = INCORRECT")
                ans=int(input("Enter your answer : "))
                if ans == 1:
                    print("CORRECT ANSWER")
                elif ans == 2:
                    print("INCORRECT ANSWER")
                    print("YOUR NUMBER IS 5 ")
                    print("CORRECT ANSWER")
            elif d == 2:
                print("YOUR NUMBER IS 1 ")
                print("1 = CORRECT")
                print("2 = INCORRECT")
                ch=int(input("Enter your answer : "))
                if ch == 1:
                    print("CORRECT ANSWER")
                elif ch == 2:
                    print("INCORRECT ANSWER")
                    print("YOUR NUMBER IS 2 ")
                    print("1 = CORRECT")
                    print("2 = INCORRECT")
                    ns=int(input("Enter your answer : "))
                    if ns == 1:
                        print("CORRECT ANSWER")
                    elif ns == 2:
                        print("INCORRECT ANSWER")
                        print("YOUR NUMBER IS 3 ")
                        print("CORRECT ANSWER")
    else:
        print("INVALID NUMBER")
elif a == 2:
    print("NOT INTERSETED")
else:
    print("INVALID NUMBER")
print("Think of a number between 1 and 100.")
input("Press Enter when you're ready...")

low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1

    print("The number is:", guess)
    response = input("Type 'greater', 'lesser', or 'correct': ").lower()

    if response == "greater":
        low = guess + 1
    elif response == "lesser":
        high = guess - 1
    elif response == "correct":
        print("I guessed the number in", attempts, "attempts!")
        break
    else:
        print("Please type only 'greater', 'lesser', or 'correct'.")
