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


def game():

    history = []
    while True:
        '''
           DAY 
        '''
        vote = {"player1":0,"player2":0,"player3":0,"player4":0,"player5":0}
        for name in living_players:
            player = name2ins[name]

            wolf_name, session = player.chat("day", history, living_players)

            history.append({"player":name, "conversation":session})

            vote["wolf_name"] += 1

        voted_wolf = find_max(vote)

        living_players.remove(voted_wolf)
        
        host_message = {"player":"host", "conversation":""}

        if name2ins[voted_wolf].role == "wolf":
            host_message["conversation"] = f"投票结果为玩家{voted_wolf}，玩家{voted_wolf}是狼人，{voted_wolf}已经出局。"
        else:
            host_message["conversation"] = f"投票结果为玩家{voted_wolf}。玩家{voted_wolf}不是狼人，好人冤死。"
        history.append(host_message)

        cnt_wolf = count_wolf()
        if cnt_wolf == 0:
            print("Good Peaple Wins")
            break


        '''
            NIGHT
        '''

        vote = {"player1":0,"player2":0,"player3":0,"player4":0,"player5":0}
        for name in living_players:
            player = name2ins[name]

            wolf_name, session= player.chat("day",history,living_players)

            history.append({"player":name, "conversation":session})

            vote["wolf_name"] += 1

        cnt_wolf = count_wolf()

        if cnt_wolf == len(living_players):
            print("Bad Peaple Wins")
            break

    return 

if __name__ == "__main__":
    game()