import json


class Player:
    VERSION = "1.5,"

    def betRequest(self, game_state):
        bets = []

        for bet in game_state['players']['bet']:
            bets.append(bet)



        my_cards = []
        ##translated_state = json.load(game_state)

        my_pot = 75
        max_bet = max(bets)

        my_index = game_state["in_action"]
        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards.append(card["rank"])
        if my_cards[0] == my_cards[1]:
            return my_pot
        else:
            max_bet

    def showdown(self, game_state):
        pass

