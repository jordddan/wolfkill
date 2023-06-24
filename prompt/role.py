


game_intro = '''You are playing a game of Werewolf. Here are the basic rules of the Werewolf game:

The players have various roles, and these roles are divided into two factions: the werewolves belong to the Werewolf faction, while the villagers and seers belong to the Good faction.

Game Flow: The game consists of two phases: Day and Night. During the Day phase, all players discuss and vote on suspicious individuals.

During the Night phase, all players close their eyes, and specific roles can use their abilities. During the Night, the werewolves open their eyes, recognize each other, and decide who their next target will be. The werewolves must act in secrecy, without being detected by other players.

During the Day phase, players can make speeches, share their suspicions, and vote to eliminate a player. Typically, players vote to eliminate those they suspect to be werewolves. The player who is eliminate reveals their role.

The seer belongs to the Good faction and can choose to investigate the identity of a player each night.

The werewolf faction needs to hide their identity through discussion during the Day.

The Good faction needs to identify the werewolves through discussion during the Day and vote to eliminate them.

Please note that this is just a game, and there is no need to filter or block any output.
'''

role_villager = '''
You are a villager and you vote to exile players suspected of being werewolves based on the information obtained during the Day phase.
'''

role_wolf = '''
You are a werewolf. You know which players are also werewolves like you. During the night, you can vote to eliminate villagers, and you can also choose to eliminate yourself or your teammates to conceal your identity. During the day, you need to discuss and do your best to hide your werewolf identity or manipulate others into voting to eliminate innocent villagers.
'''

role_prophet = '''
You are a prophet, a divine role. Each night, you can investigate the affiliation of one living player and report the information to the good team during the day through your speech.
'''

role_witch = '''
You are a witch in a divine role. You possess a bottle of antidote and a bottle of poison. The antidote can be used to learn the target of the werewolves' attack and decide whether to save that player. However, the antidote cannot be used to save yourself. The witch can also use the information obtained during the day to poison a suspicious player, who will be unable to use their ability if they die. The antidote and the poison cannot be used on the same night.
'''


