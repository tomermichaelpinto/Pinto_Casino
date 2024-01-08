# Games_Library

# Slot Machine
def slotmachine(cash = 500):
    import random
    play = "YES"
    bet = 0
    min_bet = 10
    cherry = "\U0001F352"# Cherry
    lemon = "\U0001F34B"# Lemon
    grapes = "\U0001F347"# Grapes
    watermelon = "\U0001F349" # Watermelon
    orange = "\U0001F34A" # Orange
    pineapple = "\U0001F34D" # Pineapple
    banana = "\U0001F34C" # Bannana
    peach = "\U0001F351" # Peach
    strawberry = "\U0001F353" # Strawberry
    kiwi = "\U0001F95D" # Kiwi	
    L_options = [cherry, grapes, lemon, orange]
    print()
    print("WELCOME TO THE SLOTMACHINE GAME!", cherry, lemon, grapes)
    print("Your balance is: ", cash, "$")
    while play != "NO":
        print("Min bet is:", min_bet, "$")
        play = input("Do you want to play? (Answer: YES/NO): ")
        if play.upper() == "NO":
            print()
            print("***CASH OUT!***")
            print("You got: ", cash, "$")
            return cash
        elif play.upper() == "YES":
            if cash < min_bet:
                print()
                print("You don't have enough money")
                return cash
            else:
                print()
                bet = 0
                while bet < 1 or bet > 10 or min_bet*bet > cash:
                    bet = int(input("How much would you like to double your bet? | Answers 1-10: "))
                    if bet > 10:
                        print("That's too high, please enter a smaller bet")
                        print()
                        continue
                    if bet < 1:
                        print("That's too low, please enter an higher bet")
                        print()
                        print
                    if min_bet*bet > cash:
                        print("You don't have enough money, place a lower bet")
                        print()
                bet *= min_bet
                print()
                print("      ***KACHING***")
                spinning = []
                while len(spinning) < 3:
                    spinning.append(random.choice(L_options))
                print(" =======================")
                print("|                       |")
                print("| ", spinning[0], "     ", spinning[1], "     ", spinning[2], " |")
                print("|                       |")
                print(" =======================")
                print()
                if spinning.count(cherry) == 3:
                    cash += (bet * 5)
                    print("YOU WON", bet*5, "$ !")
                    print("Your balance is:", cash)
                elif spinning.count(grapes) == 3:
                    cash += (bet * 3)
                    print("YOU WON", bet*3, "$ !")
                    print("Your balance is:", cash)
                    print()
                elif spinning.count(lemon) == 3:
                    cash += (bet * 2)
                    print("YOU WON", bet*2, "$ !")
                    print("Your balance is:", cash)
                    print()
                elif spinning.count(orange) == 3:
                    cash += (bet * 2)
                    print("YOU WON", bet*2, "$ !")
                    print("Your balance is:", cash)
                    print()
                else:
                    cash -= bet
                    print("YOU LOSE !")
                    print("-"+str(bet)+"$")
                    print("Your balance is: ", cash)
                    print()
                        
        else:
            print("Please answer YES/NO !")
            print()


#Blackjack
def blackjack(cash = 500):
    import random
    min_bet = 20
    max_bet = 40
    play = "YES"
    spade = "\U00002660" # Spade
    heart = "\U00002665" # Heart
    club = "\U00002663" # Club
    diamond = "\U00002666" # Diamond
    ten = [10,"J","Q","K"]
    card = 0
    double_options = [9,10,11]
    print()
    print("WELCOME TO THE BLACKJACK GAME!", spade, heart, club, diamond)
    while play != "NO":
        bet = 0
        print("Your balance is: ", cash, "$")
        print("Min. bet is:",min_bet, "$", "|", "Max. bet is:",max_bet, "$")
        play = input("Do you want to play? (Answer: YES/NO): ")
        if play.upper() == "NO":
            print()
            print("***CASH OUT!***")
            print("You got:", cash, "$")
            return cash
        elif play.upper() != "NO" and play.upper() != "YES":
            print()
            print("Please answer YES/NO !")
            print()
        else:
            if cash < min_bet :
                print()
                print("You don't have enough money")
                return cash
            else:
                while bet != min_bet and bet != max_bet:
                    print()
                    print("Place your bet", min_bet, "or", max_bet, ":", end = " ")
                    try:
                        bet = int(input())
                    except ValueError:                    
                        print("Oops! That's not a number, try again")
                    if bet > cash:
                        print("You don't have enough money")
                        print("Please place a lower bet")
                    elif bet < min_bet:
                        print("That's too low")
                    elif bet > max_bet:
                        print("That's too high")
                cash -= bet
                double_bet = (bet*2)*2
                cards_deck = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]*6
                player_hand_0 = []
                player_hand_1 = []
                player_hand_2 = []
                dealer_hand = []
                player_0 = 0
                player_1 = 0
                player_2 = 0 
                dealer = 0
                take_card_0 = "HIT"
                take_card_1 = "HIT"
                take_card_2 = "HIT"
                index_last_a = 0
                double = ""
                double_0 = False
                double_1 = False
                double_2 = False
                plays = []
                hands_play = []
                split = ""               
                # First withdrawal from the player
                plays.append("player 0")
                hands_play.append(player_hand_0)
                card = random.choice(cards_deck)
                if card in ten:
                    player_hand_0.append(card)
                    player_0 += 10
                    cards_deck.remove(card)
                elif card == "A":
                    player_hand_0.append(card)
                    player_0 += 11
                    cards_deck.remove(card)
                else:
                    player_hand_0.append(card)
                    player_0 += card
                    cards_deck.remove(card)
                # First withdrawal from the dealer (overt)
                card = random.choice(cards_deck)
                if card in ten:
                    dealer_hand.append(card)
                    dealer += 10
                    cards_deck.remove(card)
                elif card == "A":
                    dealer_hand.append(card)
                    dealer += 11
                    cards_deck.remove(card)
                else:
                    dealer_hand.append(card)
                    dealer += card
                    cards_deck.remove(card)
                print()
                print(" ================")
                print("|Dealer got: ", card, " |")
                print(" ================")
                # Second withdrawal from the player
                card = random.choice(cards_deck)
                if card in ten:
                    player_hand_0.append(card)
                    player_0 += 10
                    cards_deck.remove(card)
                elif card == "A":
                    player_hand_0.append(card)
                    player_0 += 11
                    cards_deck.remove(card)
                else:
                    player_hand_0.append(card)
                    player_0 += card
                    cards_deck.remove(card)
                # Second withdrawal from the dealer
                card = random.choice(cards_deck)
                if card in ten:
                    dealer_hand.append(card)
                    dealer += 10
                    cards_deck.remove(card)
                elif card == "A":
                    dealer_hand.append(card)
                    dealer += 11
                    cards_deck.remove(card)
                else:
                    dealer_hand.append(card)
                    dealer += card
                    cards_deck.remove(card)
                if dealer_hand.count("A") == 2:
                    dealer -= 10
                # Blackjack options
                # Player
                if "A" in player_hand_0 and (player_hand_0[0] in ten or player_hand_0[1] in ten): 
                    player_0 = "BLACKJACK!"
                    # Player and dealer
                    if "A" in dealer_hand and (dealer_hand[0] in ten or dealer_hand[1] in ten):
                        cash += bet
                        dealer = "BLACKJACK!"
                        print()
                        print("You had:", player_hand_0,"→", player_0)
                        print("Dealer had:", dealer_hand, "→", dealer)
                        print("PLAYER AND DEALER BLACKJACK!")
                        print("DRAW!")
                        print()
                        continue
                    # Player only
                    else: 
                        cash += int(bet*2.5)
                        print()
                        print("Dealer had:", dealer_hand,"→", dealer) 
                        print("You had:", player_hand_0, "→", player_0)
                        print("BLACKJACK!")
                        print("+"+str(int(bet*2.5))+"$")
                        print()
                        continue
                    # Dealer only
                elif "A" in dealer_hand and (dealer_hand[0] in ten or dealer_hand[1] in ten):
                    dealer = "BLACKJACK!"
                    print()
                    print("Dealer had:", dealer_hand, "→", dealer)
                    print("You had: ", player_hand_0, "→", player_0)
                    print("DEALER'S BLACKJACK!")
                    print("-"+str(bet)+"$")
                    print()
                    continue
                # Double options
                if player_0 in double_options and cash >= bet:
                    index_last_a = 0
                    print()
                    print("You got:", player_hand_0, "→", player_0)
                    print()
                    while double.upper() != "YES" and double.upper() != "NO":
                        double = input("DOUBLE? (Answer: YES/NO): ")
                        if double.upper() == "YES":
                            cash -= bet
                            double_0 = True
                            take_card_0 = "STAND"
                            card = random.choice(cards_deck)
                            if card in ten:
                                player_hand_0.append(card)
                                player_0 += 10
                                cards_deck.remove(card)
                            elif card == "A":
                                player_hand_0.append(card)
                                player_0 += 11
                                cards_deck.remove(card)
                            else:
                                player_hand_0.append(card)
                                player_0 += card
                                cards_deck.remove(card)                            
                            for i in range(index_last_a,len(player_hand_0)):
                                if player_hand_0[i] == "A" and player_0 > 21:
                                    player_0 -= 10 
                        elif double.upper() == "NO":
                            continue
                        else:
                            print()
                            print("Please answer YES/NO !")
                            print()
                # Split options
                elif (player_hand_0[0] == player_hand_0[1] or player_hand_0[0] in ten and player_hand_0[1] == 10 or player_hand_0[0] == 10 and player_hand_0[1] in ten or player_hand_0[0] in ten and player_hand_0[1] in ten) and cash >= bet:
                    print()
                    print("You got:", player_hand_0)
                    print()
                    while split.upper() != "YES" and split.upper() != "NO":
                        split = input("SPLIT? (Answer: YES/NO): ")
                        if split.upper() == "YES":
                            take_card_0 = "STAND"
                            cash -= bet
                            plays.remove("player 0")
                            hands_play.remove(player_hand_0)
                            plays.append("player 1")
                            hands_play.append(player_hand_1)
                            plays.append("player 2")
                            hands_play.append(player_hand_2)
                            player_hand_1.append(player_hand_0[0])
                            if player_hand_0[0] == "A":
                                player_1 += 11
                            elif player_hand_0[0] in ten:
                                player_1 += 10
                            else:
                                player_1 += player_hand_0[0]
                            player_hand_2.append(player_hand_0[1])
                            if player_hand_0[1] == "A":
                                player_2 += 11
                            elif player_hand_0[0] in ten:
                                player_2 += 10
                            else:
                                player_2 += player_hand_0[0]
                            player_hand_0 = []
                            player_0 = 0
                            if player_hand_1[0] == "A":
                               print("You got:", player_hand_1, "→", player_1-10, "/", player_1, "&", player_hand_2, "→", player_2-10, "/", player_2)
                               print() 
                            else:
                                print("You got:", player_hand_1, "→", player_1, "&", player_hand_2, "→", player_2)
                                print()                                
                            # First hand withdrawal (after split)
                            card = random.choice(cards_deck)
                            if card in ten:
                                player_hand_1.append(card)
                                player_1 += 10
                                cards_deck.remove(card)
                            elif card == "A":
                                player_hand_1.append(card)
                                player_1 += 11
                                cards_deck.remove(card)
                            else:
                                player_hand_1.append(card)
                                player_1 += card
                                cards_deck.remove(card)
                            # Blackjack on first hand (after split)
                            if "A" in player_hand_1 and (player_hand_1[0] in ten or player_hand_1[1] in ten): 
                                plays.remove("player 1")
                                hands_play.remove(player_hand_1)
                                player_1 = "BLACKJACK!"
                                cash += int(bet*2.5)
                                print()
                                print("Dealer had:", dealer_hand,"→", dealer) 
                                print("You had:", player_hand_1, "→", player_1)
                                print("FIRST HAND - BLACKJACK!")
                                print("+"+str(int(bet*2.5))+"$")
                                print()                                                
                            # Second hand withdrawal (after split)
                            card = random.choice(cards_deck)
                            if card in ten:
                                player_hand_2.append(card)
                                player_2 += 10
                                cards_deck.remove(card)
                            elif card == "A":
                                player_hand_2.append(card)
                                player_2 += 11
                                cards_deck.remove(card)
                            else:
                                player_hand_2.append(card)
                                player_2 += card
                                cards_deck.remove(card)
                            # Blackjack on second hand (after split)
                            if "A" in player_hand_2 and (player_hand_2[0] in ten or player_hand_2[1] in ten): 
                                plays.remove("player 2")
                                hands_play.remove(player_hand_2)
                                player_2 = "BLACKJACK!"
                                cash += int(bet*2.5)
                                print()
                                print("Dealer had:", dealer_hand,"→", dealer) 
                                print("You had:", player_hand_2, "→", player_2)
                                print("SECOND HAND - BLACKJACK!")
                                print("+"+str(int(bet*2.5))+"$")
                                print()
                                if player_1 == "BLACKJACK!" and player_2 == "BLACKJACK!":
                                    break
                            # Double on first hand (after split)
                            if player_1 in double_options and cash >= bet:
                                index_last_a = 0
                                print()
                                print("You got:", player_hand_1, "→", player_1)
                                print()
                                while double.upper() != "YES" and double.upper() != "NO":
                                    double = input("DOUBLE (first hand)? (Answer: YES/NO): ")
                                    if double.upper() == "YES":
                                        cash -= bet
                                        take_card_1 = "STAND"
                                        double_1 = True
                                        card = random.choice(cards_deck)
                                        if card in ten:
                                            player_hand_1.append(card)
                                            player_1 += 10
                                            cards_deck.remove(card)
                                        elif card == "A":
                                            player_hand_1.append(card)
                                            player_1 += 11
                                            cards_deck.remove(card)
                                        else:
                                            player_hand_1.append(card)
                                            player_1 += card
                                            cards_deck.remove(card)                            
                                        for i in range(index_last_a,len(player_hand_1)):
                                            if player_hand_1[i] == "A" and player_1 > 21:
                                                player -= 10
                            # Double on second hand (after split)
                            if player_2 in double_options and cash >= bet:
                                double = ""
                                index_last_a = 0                   
                                print()
                                print("You got:", player_hand_2, "→", player_2)
                                print()
                                while double.upper() != "YES" and double.upper() != "NO":
                                    double = input("DOUBLE (second hand)? (Answer: YES/NO): ")
                                    if double.upper() == "YES":                                        
                                        cash -= bet
                                        take_card_2 = "STAND"
                                        double_2 = True
                                        card = random.choice(cards_deck)
                                        if card in ten:
                                            player_hand_2.append(card)
                                            player_2 += 10
                                            cards_deck.remove(card)
                                        elif card == "A":
                                            player_hand_2.append(card)
                                            player_2 += 11
                                            cards_deck.remove(card)
                                        else:
                                            player_hand_2.append(card)
                                            player_2 += card
                                            cards_deck.remove(card)                            
                                        for i in range(index_last_a,len(player_hand_2)):
                                            if player_hand_2[i] == "A" and player_2 > 21:
                                                player -= 10
                            # Withdrawals loop for the first hand (after split)
                            cnt = 0
                            index_last_a = 0
                            while take_card_1 != "STAND":
                                print()
                                print("Now taking cards for the first hand")
                                print()
                                print(" ================")
                                print("|Dealer got: ", dealer_hand[0], " |")
                                print(" ================")
                                print()                         
                                # Aces options for the first hand (after split)
                                if "A" in player_hand_1:
                                    if player_hand_1.count("A") == 2 and cnt == 0:
                                        print("You got:", player_hand_1, "→", player_1-20, "/", player_1-10)
                                    elif cnt == 0: 
                                        print("You got:", player_hand_1, "→", player_1-10, "/", player_1)
                                    else:
                                        a_case_sum = 0
                                        if player_hand_1.count("A") > 1:
                                            a_case_sum += player_hand_1.count("A") - 1
                                        for note in player_hand_1:
                                            if note in ten:
                                                a_case_sum += 10
                                            elif note == "A":
                                                continue
                                            else:
                                                a_case_sum += note
                                        if a_case_sum <= 10:
                                            print("You got:", player_hand_1, "→", player_1-10, "/", player_1)
                                        else:
                                            print("You got:", player_hand_1, "→", player_1)
                                else:
                                    print("You got:", player_hand_1, "→", player_1)    
                                take_card_1 = input("Take a Card? (Answer: HIT/STAND): ")
                                if take_card_1.upper() == "HIT":
                                    card = random.choice(cards_deck)
                                    if card in ten:
                                        player_hand_1.append(card)
                                        player_1 += 10
                                        cards_deck.remove(card)
                                    elif card == "A":    
                                        player_hand_1.append(card)
                                        player_1 += 11
                                        cards_deck.remove(card)
                                    else:
                                        player_hand_1.append(card)
                                        player_1 += card
                                        cards_deck.remove(card)
                                    for i in range(index_last_a,len(player_hand_1)):
                                        if player_hand_1[i] == "A" and player_1 > 21:
                                            player_1 -= 10
                                            index_last_a = i+1
                                    cnt += 1  
                                    if player_1 >= 21:
                                        plays.remove("player 1")
                                        hands_play.remove(player_hand_1)
                                        player_1 = "BURNED!"
                                        print()
                                        print("You had:", player_hand_1, "→", player_1)
                                        print("-"+str(bet)+"$")
                                        print()    
                                        break
                                elif take_card_1.upper() == "STAND":
                                    break
                                else:
                                    print()
                                    print("Please answer HIT/STAND !")
                            # Withdrawals loop for the second hand (after split)
                            cnt = 0
                            index_last_a = 0
                            while take_card_2 != "STAND":
                                print()
                                print("Now taking cards for the second hand")
                                print()
                                print(" ================")
                                print("|Dealer got: ", dealer_hand[0], " |")
                                print(" ================")
                                print()                         
                                # Aces options for the second hand (after split)
                                if "A" in player_hand_2:
                                    if player_hand_2.count("A") == 2 and cnt == 0:
                                        print("You got:", player_hand_2, "→", player_2-20, "/", player_2-10)
                                    elif cnt == 0: 
                                        print("You got:", player_hand_2, "→", player_2-10, "/", player_2)
                                    else:
                                        a_case_sum = 0
                                        if player_hand_2.count("A") > 1:
                                            a_case_sum += player_hand_2.count("A") - 1
                                        for note in player_hand_2:
                                            if note in ten:
                                                a_case_sum += 10
                                            elif note == "A":
                                                continue
                                            else:
                                                a_case_sum += note
                                        if a_case_sum <= 10:
                                            print("You got:", player_hand_2, "→", player_2-10, "/", player_2)
                                        else:
                                            print("You got:", player_hand_2, "→", player_2)
                                else:
                                    print("You got:", player_hand_2, "→", player_2)    
                                take_card_2 = input("Take a Card? (Answer: HIT/STAND): ")
                                if take_card_2.upper() == "HIT":
                                    card = random.choice(cards_deck)
                                    if card in ten:
                                        player_hand_2.append(card)
                                        player_2 += 10
                                        cards_deck.remove(card)
                                    elif card == "A":    
                                        player_hand_2.append(card)
                                        player_2 += 11
                                        cards_deck.remove(card)
                                    else:
                                        player_hand_2.append(card)
                                        player_2 += card
                                        cards_deck.remove(card)
                                    for i in range(index_last_a,len(player_hand_2)):
                                        if player_hand_2[i] == "A" and player_2 > 21:
                                            player_2 -= 10
                                            index_last_a = i+1
                                    cnt += 1  
                                    if player_2 >= 21:
                                        plays.remove("player 2")
                                        hands_play.remove(player_hand_2)
                                        player_2 = "BURNED!"
                                        print()
                                        print("You had:", player_hand_2, "→", player_2)
                                        print("-"+str(bet)+"$")
                                        print()
                                        break
                                elif take_card_2.upper() == "STAND":
                                    break
                                else:
                                    print()
                                    print("Please answer HIT/STAND !")
                    if player_1 == "BURNED!" and player_2 == "BURNED!":
                        print()
                        print("Both hands were BURNED!")
                        break
                    elif player_1 == 21 and player_2 == 21:
                        print()
                        print("Both hands got BLACKJACK!")
                        break
                # Regular game
                # Withdrawal loop (player)
                cnt = 0
                while take_card_0 != "STAND":
                    print()
                    # Aces options for the player
                    if "A" in player_hand_0:
                        if player_hand_0.count("A") == 2 and cnt == 0:
                            print("You got:", player_hand_0, "→", player_0-20, "/", player_0-10)
                        elif cnt == 0: 
                            print("You got:", player_hand_0, "→", player_0-10, "/", player_0)
                        else:
                            a_case_sum = 0
                            if player_hand_0.count("A") > 1:
                                a_case_sum += player_hand_0.count("A") - 1
                            for note in player_hand_0:
                                if note in ten:
                                    a_case_sum += 10
                                elif note == "A":
                                    continue
                                else:
                                    a_case_sum += note
                            if a_case_sum <= 10:
                                print("You got:", player_hand_0, "→", player_0-10, "/", player_0)
                            else:
                                print("You got:", player_hand_0, "→", player_0)
                                            
                    else:
                        print("You got:", player_hand_0, "→", player_0)    
                    take_card_0 = input("Take a Card? (Answer: HIT/STAND): ")
                    if take_card_0.upper() == "HIT":
                        card = random.choice(cards_deck)
                        if card in ten:
                            player_hand_0.append(card)
                            player_0 += 10
                            cards_deck.remove(card)
                        elif card == "A":    
                            player_hand_0.append(card)
                            player_0 += 11
                            cards_deck.remove(card)
                        else:
                            player_hand_0.append(card)
                            player_0 += card
                            cards_deck.remove(card)
                        for i in range(index_last_a,len(player_hand_0)):
                            if player_hand_0[i] == "A" and player_0 > 21:
                                player_0 -= 10
                                index_last_a = i+1
                        cnt += 1  
                        if player_0 >= 21:
                            break
                    elif take_card_0.upper() == "STAND":
                        break
                    else:
                        print()
                        print("Please answer HIT/STAND !")
                if player_0 > 21:
                    plays.remove("player 0")
                    hands_play.remove(player_hand_0)
                    player_0 = "BURNED!"
                    print()
                    print("You had:", player_hand_0, "→", player_0)
                    print("-"+str(bet)+"$")
                    print()
                    continue
                # Withdrawal loop (dealer)
                cnt = 0
                index_last_a = 0
                while dealer <= 16:
                    cnt += 1
                    card = random.choice(cards_deck)
                    if card in ten:
                        dealer_hand.append(card)
                        dealer += 10
                        cards_deck.remove(card)
                    elif card == "A":
                        dealer_hand.append(card)
                        dealer += 11
                        cards_deck.remove(card)
                    else:
                        dealer_hand.append(card)
                        dealer += card
                        cards_deck.remove(card)
                    for i in range(index_last_a,len(dealer_hand)):
                        if dealer_hand[i] == "A" and dealer > 21:
                            dealer -= 10
                            index_last_a = i+1
                    if dealer > 21:
                        dealer = "BURNED!"
                        break
                # Winning/losing options (player)
                for i in range(len(plays)):
                    if plays[i] == "player 0":
                        if dealer == "BURNED!":
                            if double_0:
                                cash += double_bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("+"+str(double_bet-bet-bet)+"$")
                                print()
                            else:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("+"+str(bet)+"$")
                                print()
                        elif dealer == player_0:
                            if double_0:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("DRAW!")
                                print()
                            else:
                                cash += bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("DRAW!")
                                print()
                        elif dealer > player_0:
                            if double_0:
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("-"+str(bet*2)+"$")
                                print()
                            else:
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("-"+str(bet)+"$")
                                print()
                        else:
                            if double_0:
                                cash += double_bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("+"+str(double_bet-bet-bet)+"$")
                                print()
                            else:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_0, "→", player_0)
                                print("+"+str(bet)+"$")
                                print()
                    if plays[i] == "player 1":
                        if dealer == "BURNED!":
                            if double_1:
                                cash += double_bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("+"+str(double_bet-bet-bet)+"$")
                                print()
                            else:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("+"+str(bet)+"$")
                                print()
                        elif dealer == player_1:
                            if double_1:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("DRAW!")
                                print()
                            else:
                                cash += bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("DRAW!")
                                print()
                        elif dealer > player_1:
                            if double_1:
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("-"+str(bet*2)+"$")
                                print()
                            else:
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("-"+str(bet)+"$")
                                print()
                        else:
                            if double_1:
                                cash += double_bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("+"+str(double_bet-bet-bet)+"$")
                                print()
                            else:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_1, "→", player_1)
                                print("+"+str(bet)+"$")
                                print()    
                    if plays[i] == "player 2":
                        if dealer == "BURNED!":
                            if double_2:
                                cash += double_bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("+"+str(double_bet-bet-bet)+"$")
                                print()
                            else:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("+"+str(bet)+"$")
                                print()
                        elif dealer == player_2:
                            if double_2:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("DRAW!")
                                print()
                            else:
                                cash += bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("DRAW!")
                                print()
                        elif dealer > player_2:
                            if double_2:
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("-"+str(bet*2)+"$")
                                print()
                            else:
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("-"+str(bet)+"$")
                                print()
                        else:
                            if double_2:
                                cash += double_bet
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("+"+str(double_bet-bet-bet)+"$")
                                print()
                            else:
                                cash += bet*2
                                print()
                                print("Dealer had:", dealer_hand, "→", dealer)
                                print("You had:", player_hand_2, "→", player_2)
                                print("+"+str(bet)+"$")
                                print()
