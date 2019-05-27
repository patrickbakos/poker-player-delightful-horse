import json


class Player:
    VERSION = "2.7"

    def betRequest(self, game_state):





        my_cards_rank = []
        my_cards_suit = []
        community_cards_rank = []
        community_cards_suit = []
        all_cards_suit = []
        all_cards_rank = []


        my_index = game_state["in_action"]
        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards_rank.append(card["rank"])
            my_cards_suit.append(card["suit"])
        for card in game_state["community_cards"]:
            community_cards_rank.append(card["rank"])
            community_cards_suit.append(card["suit"])

        all_cards_rank = my_cards_rank + community_cards_rank
        all_cards_suit = my_cards_suit + community_cards_suit

        #poker
        if my_cards_rank[0] == my_cards_rank[1] and community_cards_rank.count(my_cards_rank[0]) == 2\
            or community_cards_rank.count(my_cards_rank[0]) == 3\
            or community_cards_rank.count(my_cards_rank[1]) == 3:
            return 10005000

        #szin flush
        elif my_cards_suit[0] == my_cards_suit[1] and community_cards_suit.count(my_cards_suit[0]) == 3:
            if len(community_cards_rank) == 5:
                return 200000
            else:
                return 400

        #drill
        elif my_cards_rank[0] == my_cards_rank[1]\
                and my_cards_rank[0] in community_cards_rank \
                and my_cards_rank[1] in community_cards_rank:
            if len(community_cards_rank) == 5:
                return 200000
            else:
                return 300



        #pair
        elif my_cards_rank[0] == my_cards_rank[1]\
                or my_cards_rank[0] in community_cards_rank\
                or my_cards_rank[1] in community_cards_rank:
            if len(community_cards_rank) == 5:
                return 800
            else:
                return 75
        else:
            return 10

    def showdown(self, game_state):
        pass

