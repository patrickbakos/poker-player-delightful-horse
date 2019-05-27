import json

class Player:
    VERSION = "1.2"

    def betRequest(self, game_state):
        my_cards = []
        translated_state = json.load(game_state)
        my_index = translated_state["in_action"]
        for card in translated_state["palyers"][my_index]["hole_cards"]:
            my_cards.append(card["rank"])
        last_elem = my_cards[0]
        for elem in my_cards:
            if elem == last_elem:
                pass
            else:
                return 0

        return 75

    def showdown(self, game_state):
        pass

