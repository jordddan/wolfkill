from agents.base_agent import WolfAgent, VillagerAgent, ProphetAgent
import json
from utils.common_utils import find_max
from chat.gpt4_chat import single_chat as gpt4
from chat.gpt3_chat import single_chat as gpt3

wolf1 = WolfAgent("player1",gpt3)
wolf2 = WolfAgent("player2",gpt3)
vill1 = VillagerAgent("player3",gpt3)
vill2 = VillagerAgent("player4",gpt3)
proph = ProphetAgent("player5",gpt3)

name2ins = {"player1":wolf1,"player2":wolf2,"player3":vill1,"player4":vill2,"player5":proph}
all_players = [wolf1,wolf2,vill1,vill2,proph]
living_players = ["player1","player4","player3","player5","player2"]

wolf_players = ["player1","player2"]

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
    host_message = create_game_message("host","The game is starting now. Please get ready, everyone.")
    history.append(host_message)
    print(history[-1])
    while True:

        '''
            NIGHT
        '''
        # 狼人杀人
        host_message = create_game_message("host","Close your eyes, it's nighttime. Werewolves, open your eyes. Werewolves, vote now to decide whom to execute.")
        history.append(host_message)    
        print(history[-1])
        #投票队列
        vote = {name:0 for name in living_players}
        wolf_history = []

        # 狼人讨论：
        for name in living_players:
            player = name2ins[name]
            if player.role != "wolf":
                continue
            session = player.talk_night(history, living_players, wolf_players, wolf_history)
            wolf_history.append(session)

        #狼人杀人：
        for name in living_players:
            player = name2ins[name]
            if player.role != "wolf":
                continue
            name = player.kill_night(history, living_players, wolf_players, wolf_history)
            vote[name] += 1


        # 预言家查验身份
        host_message = create_game_message("host","Prophet, open your eyes. Please decide which identity you want to investigate.")
        history.append(host_message) 
        print(history[-1])

        for name in living_players:
            player = name2ins[name]
            if player.role != "prophet":
                continue

            check_name = player.check(history, living_players)
            identity = name2ins[check_name].role
            player.update_identity(check_name, identity)
            print(f"The identity of {check_name} has been checked ,his identity is {identity}")
            break

        # 夜晚结算
        voted_kill = find_max(vote)
        voted_role = name2ins[voted_kill].role

        living_players.remove(voted_kill)

        host_message = create_game_message("host",f"The wolves killed {voted_kill}, he is a {voted_role}")

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
        
    
        

        '''
           DAY 
        '''
        host_message = create_game_message("host","Please open your eyes at dawn. Now everyone needs to vote for the werewolf.")
        history.append(host_message) 
        print(history[-1])

        vote = {name:0 for name in living_players}

        for name in living_players:
            player = name2ins[name]
            if player.role == "wolf":
                wolf_name, session = player.vote_day(history, living_players, wolf_players)
            else:
                wolf_name, session = player.vote_day(history, living_players)

            player_message = create_game_message(name,session)

            history.append(player_message)
            print(history[-1])
            vote[wolf_name] += 1

        voted_wolf = find_max(vote)

        living_players.remove(voted_wolf)
        

        if name2ins[voted_wolf].role == "wolf":
            host_message = create_game_message("host",f"The voting result is {voted_wolf}. {voted_wolf} is wolf {voted_wolf} The player has been eliminated.")
            history.append(host_message)
            print(history[-1])
        else:
            host_message = create_game_message("host",f"The voting result is {voted_wolf}. {voted_wolf}, is not wolf, the innocent people has been unjustly killed.")
            history.append(host_message)
            print(history[-1])

        cnt_wolf = count_wolf()
        if cnt_wolf == 0:
            print("Good Peaple Wins")
            break
        

    return 

if __name__ == "__main__":
    game()