import json

class Player:
    VERSION = "1.0"

    def betRequest(self, game_state):
        my_cards = []
        translated_state = json.load(game_state)

        for player in translated_state["players"]:
            if "hole_cards" in player:
                for card in player["hole_cards"]:
                    my_cards.append(card["rank"])

        last_elem = my_cards[0]
        for elem in my_cards:
            if elem == last_elem:
                pass
            else:
                return 0

        return 100

    def showdown(self, game_state):
        pass

