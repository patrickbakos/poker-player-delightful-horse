import json


class Player:
    VERSION = "1.8"

    def betRequest(self, game_state):
        ##bets = []

        ##for i in range(0, 5):
        ##    for bet in game_state['players'][i]['bet']:
        ##        bets.append(bet)



        my_cards = []
        ##translated_state = json.load(game_state)



        my_index = game_state["in_action"]
        for card in game_state["players"][my_index]["hole_cards"]:
            my_cards.append(card["rank"])
        if my_cards[0] == my_cards[1]:
            return 75
        else:
            return 10

    def showdown(self, game_state):
        pass

