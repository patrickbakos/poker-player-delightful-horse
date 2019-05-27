import json


class Player:
    VERSION = "1.4.000"

    def betRequest(self, game_state):
        game_state = json.loads(game_state)
        bets = []

        for bet in game_state['players']['bet']:
            bets.append(bet)
        pot = 20

        if max(bets) > pot:
            return 0
        else:
            return pot

        my_cards = []
        ##translated_state = json.load(game_state)
        my_index = game_state["in_action"]
        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards.append(card["rank"])
        if my_cards[0] == my_cards[1]:
            return 75
        else:
            return 0

    def showdown(self, game_state):
        pass

