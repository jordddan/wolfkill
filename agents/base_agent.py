
from utils.chat import single_chat,multi_chat
from prompt.role import role_villager, role_witch, role_wolf, role_prophet, game_intro
from prompt.output import output_villager, output_wolf_day, output_wolf_night, output_prophet_day, output_prophet_night
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
        self.output_day = output_villager
    def chat(self, time, history, living_players):

        assert time == "day"

        history_text = json.dumps(history)
        living_text = json.dumps(living_players)
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

class WolfAgent:
    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role_prompt = role_wolf
        self.output_day = output_wolf_day
        self.output_night = output_wolf_night

    def chat(self, time, history, living_players):
        if time == "day":
            history_text = json.dumps(history)
            living_text = json.dumps(living_players)
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
            history_text = json.dumps(history)
            living_text = json.dumps(living_players)
            role = f"{game_intro} \n {self.role_prompt}"
            content = f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n 这是当前还活着的玩家：{living_text}\n {self.output_night}."
            output = single_chat(content=content,role=role)
            try:
                response = json.loads(output)
            except:
                raise TypeError("The output of AI can not be converted to json")
            
            kill_name = response["name"]
            reason = response["reason"]
            session = f"我是 {self.name}, 我认为{wolf_name}是狼人，我是这么想的,{reason}"
        return kill_name, session


class ProphetAgent():

    def __init__(self, name, game_prompt=None):
        self.name = name
        self.role_prompt = role_prophet
    
    def chat(self, time, history, living_players):
        if time == "day":
            history_text = json.dumps(history)
            living_text = json.dumps(living_players)
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
            '''
                选择查看一个人的身份
            '''
            history_text = json.dumps(history)
            living_text = json.dumps(living_players)
            role = f"{game_intro} \n {self.role_prompt}"
            content = f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n 这是当前还活着的玩家：{living_text}\n {self.output_night}."
            output = single_chat(content=content,role=role)
            try:
                response = json.loads(output)
            except:
                raise TypeError("The output of AI can not be converted to json")
            
            check_name = response["name"]
        return check_name