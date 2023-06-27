from agents.base_agent import WolfAgent, VillagerAgent, ProphetAgent
import json
from utils.common_utils import find_max
from chat.gpt4_chat import single_chat as gpt4
from chat.gpt3_chat import single_chat as gpt3
import random
wolf1 = WolfAgent("玩家1",gpt4)
wolf2 = WolfAgent("玩家2",gpt4)
vill1 = VillagerAgent("玩家3",gpt3)
vill2 = VillagerAgent("玩家4",gpt3)
proph = ProphetAgent("玩家5",gpt3)
vill3 = VillagerAgent("玩家6",gpt3)
name2ins = {"玩家1":wolf1,"玩家2":wolf2,"玩家3":vill1,"玩家4":vill2,"玩家5":proph,"玩家6":vill3}
all_players = [wolf1,wolf2,vill1,vill2,proph,vill3]


wolf_players = ["玩家1","玩家2"]



def game():

    def count_wolf():
        cnt = 0
        for name in living_players:
            if name2ins[name].role == "狼人":
                cnt += 1
        return cnt 

    def create_game_message(role, session):
        return {"玩家":role, "发言":session}

    living_players = ["玩家1","玩家2","玩家3","玩家4","玩家5","玩家6"]
    random.shuffle(living_players)
    history = []
    host_message = create_game_message("主持人","游戏开始，各位请准备")
    history.append(host_message)
    print(history[-1])
    while True:

        '''
            NIGHT
        '''
        # 狼人杀人
        host_message = create_game_message("主持人","天黑请闭眼，狼人请睁眼，现在你们可以选择刀哪一位玩家")
        history.append(host_message)    
        print(history[-1])
        #投票队列
        vote = {name:0 for name in living_players}
        wolf_history = []

        # 狼人讨论：
        for name in living_players:
            player = name2ins[name]
            if player.role != "狼人":
                continue
            session = player.talk_night(history, living_players, wolf_players, wolf_history)
            wolf_history.append(session)

        #狼人杀人：
        for name in living_players:
            player = name2ins[name]
            if player.role != "狼人":
                continue
            name = player.kill_night(history, living_players, wolf_players, wolf_history)
            vote[name] += 1

        # 夜晚结算
        voted_kill = find_max(vote)
        try:
            voted_role = name2ins[voted_kill].role
        except:
            import pdb
            pdb.set_trace()

        living_players.remove(voted_kill)

        host_message = create_game_message("主持人",f"狼人杀死了 {voted_kill}, 他的身份是 {voted_role}")

        history.append(host_message)
        print(history[-1])

        print(f"现在还活着的玩家是：{living_players}")
        cnt_wolf = count_wolf()
        print(f"现在还有{cnt_wolf}个狼人")

        # 预言家查验身份
        host_message = create_game_message("主持人", "预言家请睁眼，现在你需要选择一名玩家查验他的身份")
        history.append(host_message) 
        print(history[-1])

        for name in living_players:
            player = name2ins[name]
            if player.role != "预言家":
                continue

            check_name = player.check(history, living_players)
            identity = name2ins[check_name].role
            player.update_identity(check_name, identity)
            print(f"玩家 {check_name} 的身份已经被查验 , 他的身份是 {identity}")
            break


        cnt_wolf = count_wolf()

        if cnt_wolf == len(living_players):
            host_message = create_game_message("主持人",f"狼人阵营获胜")
            history.append(host_message)
            print(history[-1])
            break
        else:
            host_message = create_game_message("主持人",f"还有好人存活，游戏继续")
            history.append(host_message)
            print(history[-1])
        
        if cnt_wolf == 0:
            print("好人阵营获胜")
            break
        if len(living_players) - cnt_wolf <= 1:
            print("狼人阵营获胜")
            break
        

        '''
           DAY 
        '''
        host_message = create_game_message("主持人","天亮请睁眼，现在你们应该选择狼人玩家进行投票。")
        history.append(host_message) 
        print(history[-1])

        vote = {name:0 for name in living_players}

        for name in living_players:
            player = name2ins[name]
            if player.role == "狼人":
                wolf_name, session = player.vote_day(history, living_players, wolf_players)
            else:
                wolf_name, session = player.vote_day(history, living_players)

            player_message = create_game_message(name,session)

            history.append(player_message)
            print(history[-1])
            vote[wolf_name] += 1

        voted_wolf = find_max(vote)

        living_players.remove(voted_wolf)
        
        try:
            if name2ins[voted_wolf].role == "狼人":
                host_message = create_game_message("主持人",f"投票结果是 {voted_wolf}. {voted_wolf} 是狼人。 玩家 {voted_wolf} 已经被淘汰")
                history.append(host_message)
                print(history[-1])
            else:
                host_message = create_game_message("主持人",f"投票结果是 {voted_wolf}. 玩家{voted_wolf}不是狼人，好人冤死。")
                history.append(host_message)
                print(history[-1])
        except:
            import pdb
            pdb.set_trace()

        print(f"现在还活着的玩家是：{living_players}")
        cnt_wolf = count_wolf()
        print(f"现在还有{cnt_wolf}个狼人")
        
        cnt_wolf = count_wolf()
        if cnt_wolf == 0:
            print("好人阵营获胜")
            return True
        if len(living_players) - cnt_wolf <= 1:
            print("狼人阵营获胜")
            return False
        

    return 

if __name__ == "__main__":
    for i in range(10):
        game()