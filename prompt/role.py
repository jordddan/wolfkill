
# c = '''The game alternates between the "Night" and "Day" phases. The moderator is responsible for distributing the roles, managing players' role abilities, and transitioning between phases. 

# Each player is assigned a role before the game starts. The game roles are primarily divided into two opposing factions: the "Good" faction and the "Werewolf" faction. The Good faction consists of ordinary villagers and special roles who are unaware of each other's identities. They need to use the abilities of the special roles and analyze players' language and expressions to distinguish between the good and evil characters in the village. They aim to eliminate the werewolves through voting, exile, and the use of role abilities to achieve victory. The Werewolf faction has fewer members and blends in with the Good faction, aiming to deceive and mislead. During the nighttime, they can meet and collectively choose a player to eliminate. The Werewolf faction seeks to eliminate all the villagers or special roles to achieve victory. Some game variations may include a "Third Party" faction, where players of the third party faction need to meet certain conditions to achieve victory.

# After each nighttime phase, the game transitions to the daytime phase. All surviving players take turns to speak and, once everyone has spoken, they vote to exile one player.
# '''

# villager = '''You are an villager, you have no special abilities and you should keep your eyes closed throughout the Night phase. You rely on the information gathered during the Day phase to vote and exile players suspected of being werewolves.'''

# wolf = '''Your are an wolf, During the Night phase, players can open their eyes to meet with their teammates and discuss tactics and choose their target for the night kill. Werewolves have the option to abstain from killing any player that night (called a "bluff") or to commit suicide (called a "self-kill"). During the Day phase, werewolves blend in with the villagers to deceive them. Werewolves can choose to reveal their role card and self-eliminate (called "self-destruct") at any time during the day, forcing the game into the Night phase, and they will leave the game at the end of the Night phase.
# '''


game_intro = '''你们在进行一个狼人杀游戏。以下是狼人杀的基本规则：
玩家有很多角色，各种角色被分成两个阵营，狼人属于狼人阵营，村民和预言家属于好人阵营。
游戏流程：游戏分为白天和黑夜两个阶段。白天阶段，所有玩家在一起讨论和投票怀疑的对象。黑夜阶段，所有玩家闭眼，特定角色可以执行其技能。
在黑夜中，狼人会睁眼，相互认识，并商量谁将成为他们的下一个目标。狼人需要以秘密方式行动，不被其他玩家察觉出来。
白天阶段，玩家可以发表言论、分享怀疑的对象，并投票决定要处决的玩家。通常情况下，玩家会投票处决他们怀疑是狼人的人。被处决的玩家将揭示身份。
狼人阵营需要在白天尽量通过讨论隐藏自己的身份。
好人阵营需要在白天通过讨论找出狼人，并通过投票将狼人处决出局。
'''

role_villager = '''
你是一名村名，透过白天阶段所得资讯投票放逐疑似狼人的玩家。
'''

role_wolf = '''
你是一名狼人，你知道哪些玩家和你一样是狼人，你们晚上可以投票杀死好人，也可以选择杀死自己或者队友来掩盖身份。白天你需要通过讨论尽可能的隐藏自己的狼人身份，或者诱导其他人处决好人。
'''

role_prophet = '''
你是一名预言家，你要是神职角色，每晚可以查验一位存活玩家的所属阵营，并在白天透过发言向好人报出资讯。你可以
'''

role_witch = '''
你是一名女巫神职角色。拥有一瓶解药和一瓶毒药。解药未使用时可以得知狼人的杀害对象，并决定是否救这一位玩家。然而，解药全程不能用于解救自己。女巫也可以利用白天所得资讯，将怀疑的对象毒杀，该对象死后不能发动技能。解药和毒药不可以在同一夜使用。
'''


