
from utils.chat import single_chat,multi_chat
from prompt.role import role_villager, role_witch, role_wolf, role_prophet, game_intro
from prompt.output import output_villager, output_wolf_day, output_wolf_talk_night, output_wolf_kill_night, output_prophet_day, output_prophet_night
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
        self.role = "villager"
        self.role_prompt = role_villager
        self.output_day = output_villager
    
    def vote_day(self, history, living_players):

        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        role_text = f"{game_intro} \n {self.role_prompt}"
        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"{self.output_day}"
        )
        
        output = single_chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"我是 {self.name}, 我认为{wolf_name}是狼人，我是这么想的,{speak}"

        return wolf_name, session

class WolfAgent:
    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role = "wolf"
        self.role_prompt = role_wolf
        self.output_day = output_wolf_day
        self.output_wolf_kill_night = output_wolf_kill_night
        self.output_wolf_talk_night = output_wolf_talk_night

    def vote_day(self, history, living_players, wolf_team_mate):

        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        role_text = f"{game_intro} \n {self.role_prompt}"
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)
        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"同样是狼人的玩家是: {team_mate_text}\n" 
                f"{self.output_day}"
        )
        
        output = single_chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"我是 {self.name}, 我认为{wolf_name}是狼人，我是这么想的,{speak}"

        return wolf_name, session

    def talk_night(self,):
        

    def chat(self, time, history, living_players):
        if time == "day":
            history_text = json.dumps(history,ensure_ascii=False,indent=2)

            living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
            role = f"{game_intro} \n {self.role_prompt}"
            content = f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n 这是当前还活着的玩家：{living_text}\n {self.output_day}."

            output = single_chat(content=content,role=role)

            try:
                response = json.loads(output)
            except:
                raise TypeError("The output of AI can not be converted to json")
            
            wolf_name = response["name"]
            reason = response["reason"]
            session = f"我是 {self.name}, 我认为{wolf_name}是狼人，我是这么想的,{reason}"
            return wolf_name, session
        else:
            history_text = json.dumps(history,ensure_ascii=False,indent=2)
            living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
            role = f"{game_intro} \n {self.role_prompt}"
            content = f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n 这是当前还活着的玩家：{living_text}\n {self.output_night}."
            output = single_chat(content=content,role=role)
            try:
                response = json.loads(output)
            except:
                raise TypeError("The output of AI can not be converted to json")
            
            kill_name = response["name"]
            reason = response["reason"]
            session = f"我是 {self.name}, 我想杀{kill_name}，我是这么想的,{reason}"
        return kill_name


class ProphetAgent():

    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role = "prophet"
        self.role_prompt = role_prophet
        self.output_day = output_prophet_day
        self.output_night = output_prophet_night
        self.identity_list = []

    def chat(self, time, history, living_players):
        if time == "day":
            '''
                投票
            '''
            history_text = json.dumps(history,ensure_ascii=False,indent=2)
            living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
            role = f"{game_intro} \n {self.role_prompt}"
            content = f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n 这是当前还活着的玩家：{living_text}\n 通过之前的身份检查，我知道{json.dumps(self.identity_list)} \n {self.output_day}."

            output = single_chat(content=content,role=role)
            try:
                response = json.loads(output)
            except:
                raise TypeError("The output of AI can not be converted to json")
            
            wolf_name = response["name"]
            reason = response["reason"]
            session = f"我是 {self.name}, 我认为{wolf_name}是狼人，我是这么想的,{reason}"
            return wolf_name, session
        else:
            '''
                选择查看一个人的身份
            '''
            history_text = json.dumps(history,ensure_ascii=False,indent=2)
            living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
            identity_text = json.dumps(self.identity_list,ensure_ascii=False,indent=2)
            role = f"{game_intro} \n {self.role_prompt}"
            content = f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n 这是当前还活着的玩家：{living_text}\n 通过之前的身份检查，我知道{identity_text}\n {self.output_night}."
            output = single_chat(content=content,role=role)
            try:
                response = json.loads(output)
            except:
                raise TypeError("The output of AI can not be converted to json")
            
            check_name = response["name"]
        return check_name


    def update_identity(self, name, identity):
        self.identity_list.append(f"我知道 {name} 是一个 {identity}")