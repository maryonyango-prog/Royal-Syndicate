from Game import Game

def play_game():
    game=Game()

    human=game.human
    pc=game.pc

    game.turn=human
    #Step 1 request to make bet
    
    human_amount=human.place_initial_bet()
    #human.update_amount_bet(human_amount)
    human.bet=human_amount
    
    pc_amount=pc.auto_match_or_raise(human_amount)
    #pc.update_amount_bet(human_amount)
    pc.bet=pc_amount

    if pc_amount=="l":
        print("Towel throwin Human won")
        return
    
    game.turn=human
    game.pot=pc_amount+human_amount
    
    k =0
    #1 betting round
    print("-------------------")
    print("Starting 1st betting round")
    print("---------------------")
    while True:
        
        if k>=1 and pc.amount==human.amount:
            #completed betting round
            break
        k=k+1

        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("PC WON THE GAME")
            return

        print("-----------------------")
        print("Human amount",human.amount)
        print("Human bet amount",human.bet)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("HUMAN WON THE GAME")
            return
        
        
        print("PC amount",pc.amount)
        print("PC bet amount",pc.bet)
        print("-----------------------")

play_game()

