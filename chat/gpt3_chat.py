import openai
import sys
sys.path.append('/workspace/qiaodan/wolf')
from func_timeout import func_set_timeout
from utils.key import key

openai.api_type = "azure"

openai.api_base = "https://mtutor-dev.openai.azure.com/"

openai.api_version = "2023-03-15-preview"

openai.api_key = key


@func_set_timeout(20)
def get_response(messages):
    response = openai.ChatCompletion.create(engine="mtutor-openai-dev",
                            messages = messages,
                            temperature=0.5,)
    return response


def single_chat(content,role=None):
    if role is None:
        role = "You are an AI assistant that helps people find information."
    messages = [
                {"role":"system","content":role},
                {"role":"user","content":content}
                ]
    res = None
    cnt = 0
    while True:
        try:
            response = get_response(messages)
            res = response["choices"][0]["message"]["content"]
            break
        except:
            cnt += 1 
        if cnt >= 5:
            break    
    if res == None:
        raise TypeError("GPT-3 Can not get the response.")
    return  res

if __name__ == "__main__":
    content = '''
    You are playing a game of Werewolf.
    You are an werewolf, what should you do during the night.
    '''
    res = single_chat(content=content)
    print(res)












'''
Werewolf, also known as Mafia, is a popular party game that involves social deduction and deception. It is typically played with a large group of people, often ranging from 7 to 20 players or more.

In Werewolf, the players are assigned different roles, usually including werewolves and villagers. The game is divided into two main phases: night and day.

During the night phase, all players close their eyes, and the moderator instructs the werewolves to open their eyes and silently choose a player to eliminate. The werewolves try to eliminate villagers without being discovered. Other roles, such as the Seer or Doctor, may have special abilities during the night phase that allow them to gain information or protect players.

Once the night phase ends, the day phase begins. All players open their eyes, and the moderator announces who was eliminated by the werewolves. The remaining players then discuss and debate to figure out who the werewolves might be. Each player tries to convince others of their innocence while trying to identify the werewolves among them.

After the discussion, the players vote to eliminate a player they believe is a werewolf. The player with the most votes is removed from the game and their role is revealed. The cycle of night and day continues until one of the following conditions is met:

All the werewolves are eliminated, resulting in a victory for the villagers.
The number of werewolves equals or exceeds the number of villagers, resulting in a victory for the werewolves.
Werewolf is a game of deduction, persuasion, and bluffing. It requires players to analyze behavior, gather information, and make strategic decisions. The game can be highly interactive and suspenseful, making it a popular choice for social gatherings and game nights.

Now you are player1, a werewolf, 
Now is the day time, you 
'''