
from utils.chat import single_chat,multi_chat
from prompt.role import role_villager, role_witch, role_wolf, role_prophet, prefix_prompt
from prompt.output import output_villager, output_wolf_day, output_worf_night, output_prophet_day, output_prophet_night
import json

class BaseAgnet:

    def __init__(self, name, role_prompt=None, game_prompt=None):
        self.role_prompt = role_prompt
        self.name = name 

    def chat():

        return 
    
class VillagerAgent:

    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role_prompt = role_villager

    def chat(time, history, ling_players):
        assert time == "day"

        history_text = json.dumps(history)


class WolfAgent:
    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role_prompt = role_wolf

    def chat(time, hitory, living_players):
        
        return 


class ProphetAgent():

    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role_prompt = role_prophet