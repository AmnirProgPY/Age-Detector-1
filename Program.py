import sys
while True:
    print("Age Detector :")
    input("Enter you're name(Optionnal): ")

    try:
        birth = int(input("enter you're birth: "))
        current_year = 2025
        current_age = current_year - birth
        print("you're age is: ", current_age)
    except ValueError :
        print("Use Numbers instead !")
    print("==========================\nPlease Select Number :\n1.Play Again\n2.Exit LOOP and Program :")
    choice = input("Enter Please You're Choice :")
    if choice == "1":
        print("Let's Play again !\n==========================")
    elif choice == "2":
        print("==========================\nGoodBye !, Now the Program will be Closed !")
        sys.exit()
    if False :
        print("There is an ERROR while Looping or Playing in this Program, Please Contact us at:\n0702939070 or +212 702 939 070")