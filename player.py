import json


class Player:
    VERSION = "2.9.5"

    def betRequest(self, game_state):





        my_cards_rank = []
        my_cards_suit = []
        community_cards_rank = []
        community_cards_suit = []
        all_cards_suit = []
        all_cards_rank = []

        my_index = game_state["in_action"]
        my_stack = game_state["players"][my_index]["stack"]

        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards_rank.append(card["rank"])
            my_cards_suit.append(card["suit"])
        for card in game_state["community_cards"]:
            community_cards_rank.append(card["rank"])
            community_cards_suit.append(card["suit"])

        all_cards_rank = my_cards_rank + community_cards_rank
        all_cards_suit = my_cards_suit + community_cards_suit


        #big stack

        if my_stack > 2999:
            return my_stack
        #poker
        elif my_cards_rank[0] == my_cards_rank[1] and community_cards_rank.count(my_cards_rank[0]) == 2\
            or community_cards_rank.count(my_cards_rank[0]) == 3\
            or community_cards_rank.count(my_cards_rank[1]) == 3:
            return my_stack

        #full
        elif len(community_cards_rank) == 3 and len(set(all_cards_rank)) == 2:
            return 500
        elif len(community_cards_rank) == 4 and ((set(all_cards_rank) == 3 or set(all_cards_rank) == 2)):
                return my_stack
        elif len(community_cards_rank) == 5 and (len(set(all_cards_rank)) == 3 or len(set(all_cards_rank)) == 4 or len(set(all_cards_rank)) == 5):
                return my_stack


        #szin flush
        elif my_cards_suit[0] == my_cards_suit[1] and community_cards_suit.count(my_cards_suit[0]) == 3:
            if len(community_cards_rank) == 5 or len(community_cards_rank) == 4:
                return my_stack
            else:
                return 400

        #drill
        elif my_cards_rank[0] == my_cards_rank[1]\
                and my_cards_rank[0] in community_cards_rank \
                and my_cards_rank[1] in community_cards_rank:
            if len(community_cards_rank) == 5:
                return my_stack
            else:
                return 300



        #pair
        elif my_cards_rank[0] == my_cards_rank[1]\
                or my_cards_rank[0] in community_cards_rank\
                or my_cards_rank[1] in community_cards_rank:
            if len(community_cards_rank) == 5:
                return 500
            else:
                return 75
        elif game_state["round"] < 5:
            return 10
        elif game_state["round"] >= 5:
            return my_stack
        else:
            return 0

    def showdown(self, game_state):
        pass

