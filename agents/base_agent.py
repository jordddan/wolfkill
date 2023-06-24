from prompt.role import role_villager, role_wolf, role_prophet, game_intro
from prompt.output import output_villager, output_wolf_day, output_wolf_talk_night, output_wolf_kill_night, output_prophet_day, output_prophet_night
import json

class BaseAgnet:

    def __init__(self, name, role_prompt=None, game_prompt=None):
        self.role_prompt = role_prompt
        self.name = name 

    def chat():

        return 
    
class VillagerAgent:

    def __init__(self, name, chat_func):
        self.name = name
        self.role = "villager"
        self.role_prompt = role_villager
        self.output_day = output_villager
        self.chat = chat_func
    def vote_day(self, history, living_players):

        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"You are {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        content = (
                f"This is the previous game content, saved in JSON format, with each entry representing a conversation: {history_text}\n"
                f"These are the players who are currently alive: {living_text}\n"
                f"{self.output_day}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"I am {self.name}, I think {wolf_name} is wolf, here is what I thought {speak}"
        print(f"{self.name}, {output}")
        return wolf_name, session

class WolfAgent:
    def __init__(self, name, chat_func):
        self.name = name
        self.role = "wolf"
        self.role_prompt = role_wolf
        self.output_day = output_wolf_day
        self.output_wolf_kill_night = output_wolf_kill_night
        self.output_wolf_talk_night = output_wolf_talk_night

        self.chat = chat_func
    def vote_day(self, history, living_players, wolf_team_mate):

        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"You are {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)

        content = (
                f"This is the previous game content, saved in JSON format, with each entry representing a conversation: {history_text}\n"
                f"These are the players who are currently alive:{living_text}\n"
                f"The players who are also werewolves are: {team_mate_text}\n" 
                f"{self.output_day}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            import pdb
            pdb.set_trace()
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"I am {self.name}, i think {wolf_name}is wolf, here is what I thought {speak}"
        print(f"{self.name}, {response}")
        return wolf_name, session

    def talk_night(self, history, living_players, wolf_team_mate, wolf_history):
        
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"You are {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)
        wolf_history_text = json.dumps(wolf_history,ensure_ascii=False,indent=2)
        content = (
                f"This is the previous game content, saved in JSON format, with each entry representing a conversation: {history_text}\n"
                f"These are the players who are currently alive:{living_text}\n"
                f"The players who are also werewolves are: {team_mate_text}\n" 
                f"These are the previous statements of your wolf teammates: {wolf_history_text}\n"
                f"{self.output_wolf_talk_night}"
        )


        output = self.chat(content=content,role=role_text)

        session = f"I am {self.name}, {output}"
        print(f"{self.name}, {output}")
        return session


    def kill_night(self, history, living_players, wolf_team_mate, wolf_history):
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"You are{self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)
        wolf_history_text = json.dumps(wolf_history,ensure_ascii=False,indent=2)

        content = (
                f"This is the previous game content, saved in JSON format, with each entry representing a conversation: {history_text}\n"
                f"These are the players who are currently alive: {living_text}\n"
                f"The players who are also werewolves are: {team_mate_text}\n" 
                f"These are the previous statements of your wolf teammates:  {wolf_history_text}\n"
                f"{self.output_wolf_kill_night}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        kill_name = response["name"]
        thought = response["thought"]
        session = f"I am  {self.name}, i want to kill {kill_name}, here is what I thought: {thought}"
        print(session)
        print(f"{self.name}, {response}")
        return kill_name


class ProphetAgent():

    def __init__(self, name, chat_func):
        self.name = name
        self.role = "prophet"
        self.role_prompt = role_prophet
        self.output_day = output_prophet_day
        self.output_check = output_prophet_night
        self.identity_list = []
        self.chat = chat_func
    def vote_day(self, history, living_players):
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        identity_text = json.dumps(self.identity_list,ensure_ascii=False,indent=2)
        name_text = f"You are {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        content = (
                f"This is the previous game content, saved in JSON format, with each entry representing a conversation: {history_text}\n"
                f"These are the players who are currently alive: {living_text}\n"
                f"This is the player identity information that you already know: {identity_text}"
                f"{self.output_day}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"I am  {self.name}, I think {wolf_name} is wolf, here is what I thought: {speak}"
        print(f"{self.name}, {response}")
        return wolf_name, session

    def check(self, history, living_players):
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        identity_text = json.dumps(self.identity_list,ensure_ascii=False,indent=2)
        name_text = f"你是{self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        content = (
                f"This is the previous game content, saved in JSON format, with each entry representing a conversation: {history_text}\n"
                f"These are the players who are currently alive:{living_text}\n"
                f"This is the player identity information that you already know: {identity_text}"
                f"{self.output_check}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        check_name = response["name"]
        print(f"{self.name}, {response}")
        return check_name

    def update_identity(self, name, identity):
        self.identity_list.append(f"I know {name} is {identity}")