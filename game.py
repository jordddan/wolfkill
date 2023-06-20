from agents.base_agent import WolfAgent, VillagerAgent, ProphetAgent
import json
from utils.common_utils import find_max
wolf1 = WolfAgent("player1")
wolf2 = WolfAgent("player2")
vill1 = VillagerAgent("player3")
vill2 = VillagerAgent("player4")
proph = ProphetAgent("player5")
name2ins = {"player1":wolf1,"player2":wolf2,"player3":vill1,"player4":vill2,"player5":proph}
all_players = [wolf1,wolf2,vill1,vill2,proph]
living_players = ["player1","player4","player3","player5","player2"]




def count_wolf():
    cnt = 0
    for name in living_players:
        if name2ins[name].role == "wolf":
            cnt += 1
    return cnt 

def create_game_message(role, session):

    return {"player":role, "conversation":session}


def game():

    history = []
    host_message = create_game_message("host","现在游戏开始，请大家做好准备")
    history.append(host_message)
    print(history[-1])
    while True:

        '''
            NIGHT
        '''
        # 狼人杀人
        host_message = create_game_message("host","天黑请闭眼。狼人请睁眼，狼人请投票决定杀人")

        vote = {"player1":0,"player2":0,"player3":0,"player4":0,"player5":0}

        history.append(host_message)    

        # import pdb
        # pdb.set_trace()

        print(history[-1])
        # 狼人杀人：
        for name in living_players:
            player = name2ins[name]
            if player.role != "wolf":
                continue
            kill_name = player.chat("night", history, living_players)
            vote[kill_name] += 1
        
        voted_kill = find_max(vote)
        voted_role = name2ins[voted_kill].role

        living_players.remove(voted_kill)

        host_message = create_game_message("host",f"狼人杀死了{voted_kill},被杀死的玩家的身份是{voted_role}")

        history.append(host_message)
        print(history[-1])


        wolf_num = count_wolf()
        if wolf_num == len(living_players):
            host_message = create_game_message("host",f"好人全部被杀死，狼人获胜")
            history.append(host_message)
            print(history[-1])
            break
        else:
            host_message = create_game_message("host",f"还有好人存活，游戏继续")
            history.append(host_message)
            print(history[-1])
        
        # 预言家查验身份
        host_message = create_game_message("host","预言家请睁眼，请决定你要查验的身份")
        history.append(host_message) 
        print(history[-1])
        for name in living_players:
            player = name2ins[name]
            if player.role != "prophet":
                continue

            check_name = player.chat("night", history, living_players)
            identity = name2ins[check_name].role
            player.update_identity(check_name, identity)
            print(f"验查了玩家{check_name},身份是{identity}")
        

        '''
           DAY 
        '''
        host_message = create_game_message("host","天亮请睁眼，现在每个人需要对狼人投票")
        history.append(host_message) 
        print(history[-1])

        vote = {"player1":0,"player2":0,"player3":0,"player4":0,"player5":0}

        for name in living_players:
            player = name2ins[name]

            wolf_name, session = player.chat("day", history, living_players)

            player_message = create_game_message(name,session)

            history.append(player_message)
            print(history[-1])
            vote[wolf_name] += 1

        voted_wolf = find_max(vote)

        if voted_wolf not in living_players:
            import pdb
            pdb.set_trace()
        living_players.remove(voted_wolf)
        
        host_message = create_game_message("host","天亮请睁眼，现在每个人需要对狼人投票")
        history.append(host_message)
        print(history[-1])

        if name2ins[voted_wolf].role == "wolf":
            host_message = create_game_message("host",f"投票结果为玩家{voted_wolf}，玩家{voted_wolf}是狼人，{voted_wolf}已经出局。")
            history.append(host_message)
            print(history[-1])
        else:
            host_message = create_game_message("host",f"投票结果为玩家{voted_wolf}。玩家{voted_wolf}, 不是狼人，好人冤死。")
            history.append(host_message)
            print(history[-1])

        cnt_wolf = count_wolf()
        if cnt_wolf == 0:
            print("Good Peaple Wins")
            break

    return 

if __name__ == "__main__":
    game()