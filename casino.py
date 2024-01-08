import games_library

def casino(cash = 500):
    money = "\U0001F4B0"+"\U0001F4B0"+"\U0001F4B0" # Money Bags
    play = "YES"
    games = ["blackjack", "slotmachine"]
    age = ""
    while age != "YES" and age != "NO":
        age = input("Is your age 21+? Answer - (YES/NO): ").upper()
        if age == "NO":
            return "YOU ARE TOO YOUNG AND ARE NOT ALLOWED TO PLAY!"
    while play != "NO":
        print()
        print("WELCOME TO PINTO CASINO !", money)
        print("Your balance is:", cash, "$")
        play = input("Do you want to play? Answer - (YES/NO): ")
        if play.upper() == "NO":
            print("***CASH OUT!***")
            print("You got:", cash, "$")
            print("See you soon!")
            break
        else:
            print()
            print("Enjoy your stay!")
            choose_game = ""
            while choose_game not in games:
                print("Please choose a game to play from the list -", games, ":")
                choose_game = input()
                if choose_game.lower() == "blackjack":
                    cash = games_library.blackjack(cash)
                    break
                if choose_game.lower() == "slotmachine":
                    cash = games_library.slotmachine(cash)                    
                    break                    
