class Card():
    
    RANKS=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    SUITES=["HEARTS","DIAMONDS","SPADES","CLUBS"]
    
    def __init__(self,suite,rank):

        if not isinstance(suite,str):
            raise TypeError(f"Suite expected to be a string got {type(suite).__name__}")
        
        if not isinstance(rank,str):
            raise TypeError(f"Rank expected to be a string got {type(rank).__name__}")

        # Normalize the strings to uppercase
        suiteUpper=suite.upper()
        rankUpper=rank.upper()
        if rankUpper in Card.RANKS:
            pass
        else:
            raise TypeError(f"Added rank is not in rank list {Card.RANKS}")

        if suiteUpper in Card.SUITES:
            pass
        else:
            raise TypeError(f"Added suite is not in suite list {Card.SUITES}")

        # Assign properties to the card instance
        self.rank=rankUpper
        self.suite=suiteUpper
        
    def print_card(self):
        print("Rank",self.rank)
        print("Suite",self.suite)

if __name__=="__main__":
    # Test with an invalid suite which should raise a TypeError
    try:
        card1=Card(suite="Joker",rank="A")
        card1.print_card()
    except TypeError as e:
        print(f"Error: {e}")
    
    # Test with valid parameters
    card2=Card(suite="Clubs",rank="3")
    card2.print_card()


        
