class GoFish:

    #Role of computer and players
    #Computer can know what cards are in the pool
    #and what cards each player has
    #Computer has to track the number of books (sets of 4 cards) that have been laid down
    #Computer has to let them know when one player has won so it has to track the number of book each player has
    #Players have to be able to ask one other player if they have any of a card they already have like eights
    #That player has to be able to respond to that player by giving him all of this cards of that value
    #if they have it or tell them go fish
    #if they have it, computer has to remove those cards from the list of cards that player 2 has and add them to the list of cards 
    #player 1 has
    #if they hear go fish, Computer has to allow player 1 to pick a card from the pool


    #Approach 1:
    #Data Structures
    #   int variable to store numOfPlayers
    ##  int variable to store totalNumberOfBooks
    #   list[int] to store number of books that each player has
    #   list[string] to store cards in pool
    #   list[Player] to store Players
    #   Player object 
    #       int number
    #       String name
    #       list[string] to store cards each player has
    #Functions
    #welcome()
    #ask_how_many_players_there()
    #ask_player_x_name(int playerNum)
    #deal_cards()
    #string ask_player_who_they_want_to_ask(String name)
    #string ask_player_what_card_they_want_to_ask_for(String name)
    #string ask_responding_player_to_say_number_of_cards_or_go_fish(String name)
    #update_players_cards(int askPlayerNum, int respondingPlayerNum)
    #randomly_deal_card_to_player(int playerNum)
    num_of_players = 0
    POSSIBLE_NUMBER_OF_BOOKS = 13
    current_number_of_books_total = 0
    number_books_of_each_player = []
    cards_in_pool = []
    players = []


    class Player:
        number = 0
        name = ''
        cards = []

        def __init__(self, number, name, cards):
            self.number = number
            self.name = name
            self.cards = cards


    def get_num_of_players(self):
        return input("Welcome to Go Fish! How many players will be playing? ")        

    def startGame(self):
        num_of_players = self.get_num_of_players();
        print(num_of_players)
        # self.Player = self.Player(1, "Karthik", [])


if __name__== '__main__':
    goFish = GoFish()
    goFish.startGame()