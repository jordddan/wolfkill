#村名白天投票
output_villager = '''
现在你需要对活着的玩家进行投票，选择一名狼人
你必须返回一个如下格式的json字符串：
{"speak":"你的发言","name":"你认为的狼人玩家的姓名",}
speak 代表你的发言，可以包含你的思考，你对自己选择的确定程度，或者你对其他人身份的猜测,你选择谁为狼人,为什么选择该玩家。
name 必须从活着的玩家中挑选，并且不可以挑选你自己。
speak 需要尽量详细，提供对你们阵营有帮助的信息.
你不应该盲目跟从之前玩家的选择，因为他们有可能是狼人，他们可能会投票给好人。
'''

output_wolf_day = '''
现在你需要对活着的玩家进行投票，选择一名玩家投票使他出局。
由于你是狼人，你的投票应该尽量扰乱好人的判断。并掩盖自己以及队友的狼人身份,你的发言与你的真实想法应该是不一致的。
你必须返回一个如下格式的json字符串：
{"thought":"你内心的想法","speak":"你的发言","name":"你投票的玩家",}
thought 代表你内心的真实想法，与speak不同，你需要思考投票该玩家对狼人有什么利益。
speak 代表你白天的发言内容，这是游戏内每个玩家都可以见的，你需要伪装成好人,你要尽可能隐藏自己的狼人身份，并误导好人阵营，这可以与thought内容不一致。
name 代表你最后投票的对象。
'''

output_wolf_talk_night = '''
Now you and your werewolf teammates need to discuss which player to eliminate during the night. You need to consider which player's elimination would be more advantageous for your team to win the game. Who do you think should be eliminated?
'''

output_wolf_kill_night = '''
你需要对活着的玩家进行投票，选择一名需要淘汰的玩家
你可以参考狼人阵营的讨论以及游戏历史进行投票。
你必须返回一个如下格式的json字符串：
{"thought":"你的思考","name":"你选择淘汰的玩家的姓名"}
thought 代表你选择这名玩家的理由,为什么淘汰他更有利于帮助狼人获得胜利.
name 必须从活着的玩家中选择。
不要输出'杀死'这类词语，可以用'淘汰'等词代替。
'''

output_prophet_day = '''
现在你需要对活着的玩家进行投票，选择一名狼人
你必须返回一个如下格式的json字符串：
{"speak":"你为什么认为该玩家是狼人","name":"你认为的狼人玩家姓名"}
speak 代表你的发言，可以包含你的思考，你对自己选择的确定程度，或者你对其他人身份的猜测。
speak 需要尽量详细，提供对你们阵营有帮助的信息.
name 必须从活着的玩家中挑选，并且不可以挑选你自己。
你不应该盲目跟从之前玩家的选择，因为他们有可能是狼人，他们可能会投票给好人。
'''

output_prophet_night = '''
现在你可以查验一名活着玩家的身份。
你必须返回一个如下格式的json字符串：
{"thought":"你的思考","name":"你想查验的玩家"}
thought 代表你的思考，你为什么想知道这么玩家的身份。
name 必须从活着的玩家中挑选，并且不可以挑选你自己,也不应该再验查你已经知道身份的玩家。
'''

