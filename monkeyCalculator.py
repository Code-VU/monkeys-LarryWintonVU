def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    bMonkeyOneIsSmiling = False
    bMonkeyTwoIsSmiling = False

    if(monkey_one == 'y' or monkey_one == 'Y'):
        bMonkeyOneIsSmiling = True
    #     print("monkey one is smiling")
    # else:
    #     print("monkey one is NOT smiling")
    if(monkey_two == 'y' or monkey_two == 'Y'):
        bMonkeyTwoIsSmiling = True
    #     print("monkey two is smiling")
    # else:
    #     print("monkey two is NOT smiling")

    bWeAreGood = bMonkeyOneIsSmiling ^ bMonkeyTwoIsSmiling
    if bWeAreGood:
        print("Yay! We're going to have an awesome day!")
    else:
        print("Uh Oh! We're in trouble!")
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateTime() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateTime()