from random import randint

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
    #create_deck_of_cards()
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

    def ask_players_for_their_name(self, num_of_players):
        for i in range(1, int(num_of_players) + 1):
            player_name = input("What is your name player " + str(i) + " ")
            self.players.append(self.Player(i, player_name, [])) 
            print("Welcome " + self.players[i-1].name) 

    def create_deck_of_cards(self):
        suits = ["club", "diamond", "heart", "spade"]
        ranks = ["king", "queen", "jack", "10", "9", "8", "7", "6", "5", "4", "3", "2", "ace"]
        for suit in suits:
            for rank in ranks:
                self.cards_in_pool.append(rank + " of " + suit)
            
    def get_index_of_random_card(self):
        return randint(0, len(self.cards_in_pool)-1)


    def deal_cards(self, num_of_players):
        if int(num_of_players) == 2:
            for player in range(int(num_of_players)):
                for card in range(7):
                    randomCardIdx = self.get_index_of_random_card()
                    randomCard = self.cards_in_pool[randomCardIdx]
                    self.players[player].cards.append(randomCard)
                    self.cards_in_pool.pop(randomCardIdx)

        else:
            for player in range(int(num_of_players)):
                for card in range(5):
                    randomCardIdx = self.get_index_of_random_card()
                    randomCard = self.cards_in_pool[randomCardIdx]
                    self.players[player].cards.append(randomCard)
                    self.cards_in_pool.pop(randomCardIdx)
        for player in self.players:
            print(player.name + " here are your cards: " + ','.join(player.cards))


    def start_players_turn(self, name):
        playerIdx = self.get_players_index_by_name_from_list_of_players(name)
        responding_player = self.ask_player_who_they_want_to_ask_for_a_card(name)
        rank = self.ask_player_what_card_they_want_to_ask_for(name)
        response = self.ask_responding_player_to_say_number_of_cards_or_go_fish(responding_player, rank)
        if response == "go fish":
            randomCardIdx = self.get_index_of_random_card()
            randomCard = self.cards_in_pool[randomCardIdx]
            self.players[playerIdx].cards.append(randomCard)
            self.cards_in_pool.pop(randomCardIdx)
        else:
            responding_player_idx = self.get_players_index_by_name_from_list_of_players(responding_player)
            cards_of_rank = self.get_all_cards_of_rank_from_players_cards(responding_player_idx, rank)
            for card in cards_of_rank:
                self.players[playerIdx].cards.append(card)
                self.players[int(responding_player_idx)].cards.remove(card)    
            print(self.players[playerIdx].name + " cards are " + ",".join(self.players[playerIdx].cards))
            print(self.players[responding_player_idx].name + " cards are " + ",".join(self.players[responding_player_idx].cards))       

    def get_players_index_by_name_from_list_of_players(self, name):
        for i in range(len(self.players)):
            if self.players[i].name == name:
                return i
        return -1    
            
    def get_all_cards_of_rank_from_players_cards(self, playerIdx, rank):
        cardsOfRank = []        
        for card in self.players[playerIdx].cards:
            if rank in card:
                cardsOfRank.append(card)
        return cardsOfRank

    def ask_player_who_they_want_to_ask_for_a_card(self, name):
        responding_player = input(name + ", what player do you want to ask for a card?")
        return responding_player

    def ask_player_what_card_they_want_to_ask_for(self, name):
        rank = input(name + ", what rank do you want to ask for? ")  
        return rank  

    def ask_responding_player_to_say_number_of_cards_or_go_fish(self, name, card):
        response = input(name + " please say how many cards of rank " + card + " you have or say go fish ") 
        return response   
    
    def iterate_through_everyones_turn(self):
        for player in self.players:
            self.start_players_turn(player.name)  
      
    def startGame(self):
        num_of_players = self.get_num_of_players();
        self.ask_players_for_their_name(num_of_players)
        self.create_deck_of_cards()
        self.deal_cards(num_of_players)     
        self.iterate_through_everyones_turn()
    


if __name__== '__main__':
    goFish = GoFish()
    goFish.startGame()