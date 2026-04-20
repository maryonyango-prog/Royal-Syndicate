from Card import Card
import random

class Deck():
    """
    Representing a full standard deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initializes the deck by generating 52 unique Card objects
        based on all possible ranks and suites.
        """
        ranks = Card.RANKS
        suites = Card.SUITES
        deck = [] # The list to hold the Card objects
        
        for rank in ranks:
            for suite in suites:
                card = Card(suite=suite, rank=rank)
                deck.append(card)
        self.deck=deck

    #Randomizes order of the cards in the deck.
    def shuffle(self):
        
        newDeck = []
        deck = self.deck
        
        while True:
            if len(deck) == 1:
                card = deck[0]
                newDeck.append(card)
                break
                
            n = random.randint(0, len(deck) - 1)
            
            # Remove a random card from the current deck and add it to the new shuffled deck
            card = deck[n]
            deck.pop(n)
            newDeck.append(card)
            
        print("new Deck length", len(newDeck))
        print("old deck length", len(deck))
        
        for card in newDeck:
            card.print_card()
            print("--")
            
        self.deck = newDeck
        
    #Print out the suite and rank of every card in the deck.
    def print_deck(self):
        deck = self.deck
        print("Deck size is", len(deck))
        print("...............")
        for card in deck:
            card.print_card()
            print("___________")

    #Removes the top card from the deck and places it at the bottom called Burning
    def burn_card(self):
        
        print("before buring deck")
        self.print_deck()
        print("After buring")
        top_card = self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        self.print_deck()

    #take a card out of the deck from the end deck and give it out
    def give_card(self):
       
        top_card=self.deck[0]
        self.deck.pop(0)
        return top_card

if __name__ == "__main__":
    d1 = Deck()
    d1.shuffle()
    #d1.burn_card()
    card = d1.give_card()
    print("given card is")
    card.print_card()
    d1.print_deck()

