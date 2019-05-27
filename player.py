import json


class Player:
    VERSION = "1.8"

    def betRequest(self, game_state):
        ##bets = []

        ##for i in range(0, 5):
        ##    for bet in game_state['players'][i]['bet']:
        ##        bets.append(bet)



        my_cards_rank = []
        community_cards_rank = []
        community_cards_suit = []
        ##translated_state = json.load(game_state)



        my_index = game_state["in_action"]
        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards_rank.append(card["rank"])
        for card in game_state["community_cards"]:
            community_cards_rank.append(card["rank"])
            community_cards_suit.append(card["suit"])
        if my_cards_rank[0] == my_cards_rank[1]\
                or my_cards_rank[0] in community_cards_rank\
                or my_cards_rank[1] in community_cards_rank:
            return 300
        elif my_cards_rank[0] == my_cards_rank[1]\
                or my_cards_rank[0] in community_cards_rank \
                or my_cards_rank[1] in community_cards_rank:
            return 75

        else:
            return 10

    def showdown(self, game_state):
        pass

