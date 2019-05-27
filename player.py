import json

class Player:
    VERSION = "1.4.000"

    def betRequest(self, game_state):
        my_cards = []
        translated_state = json.load(game_state)
        my_index = translated_state["in_action"]
        for card in translated_state["players"][my_index]["hole_cards"]:
            my_cards.append(card["rank"])
        if my_cards[0] == my_cards[1]:
            return 75
        else:
            return 0

    def showdown(self, game_state):
        pass

