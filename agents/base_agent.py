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
        self.role = "平民"
        self.role_prompt = role_villager
        self.output_day = output_villager
        self.chat = chat_func
    def vote_day(self, history, living_players):

        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"你是 {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"{self.output_day}"
        )

        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"我是 {self.name}, 我认为 {wolf_name} 是狼人, 这是我的想法 {speak}"
        return wolf_name, session

class WolfAgent:
    def __init__(self, name, chat_func):
        self.name = name
        self.role = "狼人"
        self.role_prompt = role_wolf
        self.output_day = output_wolf_day
        self.output_wolf_kill_night = output_wolf_kill_night
        self.output_wolf_talk_night = output_wolf_talk_night

        self.chat = chat_func

    def vote_day(self, history, living_players, wolf_team_mate):

        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"你是 {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)

        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"同样是狼人的玩家是: {team_mate_text}\n" 
                f"{self.output_day}"
        )

        # print(f"狼人白天投票：{content}")

        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            import pdb
            pdb.set_trace()
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"我是 {self.name}, 我认为 {wolf_name} 是狼人, 这是我的想法 {speak}"
        # print(f"狼人白天思考：{response['thought']}")
        return wolf_name, session

    def talk_night(self, history, living_players, wolf_team_mate, wolf_history):
        
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"你是{self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)
        wolf_history_text = json.dumps(wolf_history,ensure_ascii=False,indent=2)
        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"同样是狼人的玩家是: {team_mate_text}\n" 
                f"这是之前你的狼人队友们的聊天: {wolf_history_text}\n"
                f"{self.output_wolf_talk_night}"
        )

        # print(f"狼人晚上谈话前内容：{content}")
        # print(f"狼人晚上谈话前角色：{role_text}")
        output = self.chat(content=content,role=role_text)

        session = f"我是 {self.name}, {output}"
        # print(f"狼人晚上谈话后:{session}")
        return session


    def kill_night(self, history, living_players, wolf_team_mate, wolf_history):
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        name_text = f"你是 {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        team_mate_text = json.dumps(wolf_team_mate,ensure_ascii=False,indent=2)
        wolf_history_text = json.dumps(wolf_history,ensure_ascii=False,indent=2)

        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"同样是狼人的玩家是: {team_mate_text}\n" 
                f"这是之前你的狼人队友们的聊天: {wolf_history_text}\n"
                f"{self.output_wolf_kill_night}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        kill_name = response["name"]
        thought = response["thought"]
        session = f"我是  {self.name}, 我想刀 {kill_name}, 这是我的想法 {thought}"

        print(f"狼人夜间谈话：{session}")
        return kill_name


class ProphetAgent():

    def __init__(self, name, chat_func):
        self.name = name
        self.role = "预言家"
        self.role_prompt = role_prophet
        self.output_day = output_prophet_day
        self.output_check = output_prophet_night
        self.identity_list = []
        self.chat = chat_func
    def vote_day(self, history, living_players):
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        identity_text = json.dumps(self.identity_list,ensure_ascii=False,indent=2)
        name_text = f"你是 {self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"这是你已经知道的玩家身份信息: {identity_text}"
                f"{self.output_day}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        wolf_name = response["name"]
        speak = response["speak"]
        session = f"我是 {self.name}, 我认为 {wolf_name} 是狼人, 这是我的想法 {speak}"
        return wolf_name, session

    def check(self, history, living_players):
        history_text = json.dumps(history,ensure_ascii=False,indent=2)
        living_text = json.dumps(living_players,ensure_ascii=False,indent=2)
        identity_text = json.dumps(self.identity_list,ensure_ascii=False,indent=2)
        name_text = f"你是{self.name}"
        role_text = f"{game_intro} \n {name_text}, {self.role_prompt}\n "
        content = (
                f"这是之前的游戏内容，保存为json格式，每一条是一次对话：{history_text}\n"
                f"这是当前还活着的玩家：{living_text}\n"
                f"这是你已经知道的玩家身份信息: {identity_text}"
                f"{self.output_check}"
        )
        
        output = self.chat(content=content,role=role_text)
        try:
            response = json.loads(output)
        except:
            raise TypeError("The output of AI can not be converted to json")
        
        check_name = response["name"]
        print(f"我查验了 {self.name} 的身份, 他的身份是 {response}")
        return check_name

    def update_identity(self, name, identity):
        self.identity_list.append(f"我知道 {name} 的身份是 {identity}")