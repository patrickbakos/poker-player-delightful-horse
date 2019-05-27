import json


class Player:
    VERSION = "1.1"

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

    def showdown(self, game_state):
        pass

