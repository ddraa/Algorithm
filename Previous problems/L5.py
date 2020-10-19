from _collections import deque

def solution(cards):
    cards = deque(cards)
    answer = -1

    player = []
    dealer = []
    P_turn = True
    cost = 0
    k = 0
    while cards:
        card = cards.popleft()
        if card > 10:
            card = 10
        if P_turn:
            player.append(card)
            P_turn = False
        else:
            dealer.append(card)
            P_turn = True
        #print(player, dealer)
        if len(player) == 2 and len(dealer) == 2: # game start #######
            if (1 in player and sum(player)== 11) or sum(player) == 21 : # blackjack
                if not(1 in dealer and sum(dealer) == 11): # not
                    #print(player, dealer)
                    cost += 3
                player = []
                dealer = []
                continue ### reset
            elif sum(player) < 21:
                if dealer[-1] == 1 or dealer[-1] >=7:
                    while sum(player) < 17:
                        if cards:
                            card = cards.popleft()
                            if card > 10:
                                card = 10
                            player.append(card) #### 수정
                        else:
                            return cost

                elif dealer[-1] == 4 or dealer[-1] == 5 or dealer[-1] == 6 :
                    pass

                    ## noting
                elif dealer[-1] == 2 or dealer[-1] == 3 :
                    while sum(player) < 12:
                        if card:
                            card = cards.popleft()
                            if card > 10:
                                card = 10
                            player.append(card) #### 수정
                        else:
                            return cost

            elif sum(player) > 21:## lose
                cost -= 2
                player = []
                dealer = []
                continue
            if (1 in dealer and sum(dealer) == 11) or sum(dealer) == 21:  # blackjack
                cost -= 2
                player = []
                dealer = []
                continue
            while sum(dealer) < 17:
                #print(player, dealer)
                if cards:
                    card = cards.popleft()
                    if card > 10:
                        card = 10
                    dealer.append(card)  ####
                else: ## draw
                    player = []
                    dealer = []
                    break
            #print("Fwefew")
            #print(player, dealer)
            if sum(dealer) > 21:
                cost += 2 ### player win
                player = []
                dealer = []
                continue

            if sum(player) == sum(dealer):
                pass
            elif sum(player) > sum(dealer):
                cost += 2

            else:
                cost -= 2


            #print(player, dealer)

            player = []
            dealer = []
            continue
        #print(cards)
    return cost


print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]))