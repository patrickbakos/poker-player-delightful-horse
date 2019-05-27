import json


class Player:
    VERSION = "1.8"

    def check_for_drill(self, game_state):

    def betRequest(self, game_state):





        my_cards_rank = []
        community_cards_rank = []
        community_cards_suit = []


        my_index = game_state["in_action"]
        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards_rank.append(card["rank"])
        for card in game_state["community_cards"]:
            community_cards_rank.append(card["rank"])
            community_cards_suit.append(card["suit"])

        #poker
        if my_cards_rank[0] == my_cards_rank[1] and community_cards_rank.count(my_cards_rank[0]) == 2\
            or community_cards_rank.count(my_cards_rank[0]) == 3\
            or community_cards_rank.count(my_cards_rank[1]) == 3:
            return 500

        #drill
        elif my_cards_rank[0] == my_cards_rank[1]\
                and my_cards_rank[0] in community_cards_rank \
                and my_cards_rank[1] in community_cards_rank:
            return 300

        #pair
        elif my_cards_rank[0] == my_cards_rank[1]\
                or my_cards_rank[0] in community_cards_rank\
                or my_cards_rank[1] in community_cards_rank:
            return 75
        else:
            return 10

    def showdown(self, game_state):
        pass

