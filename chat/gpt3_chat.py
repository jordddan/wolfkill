import openai
import sys
sys.path.append('/workspace/qiaodan/wolf')
from utils.key import key

openai.api_type = "azure"

openai.api_base = "https://mtutor-dev.openai.azure.com/"

openai.api_version = "2023-03-15-preview"

openai.api_key = key

def single_chat(content,role=None):


    if role is None:
        role = "You are an AI assistant that helps people find information."
    messages = [
                {"role":"system","content":role},
                {"role":"user","content":content}
                ]
    flag = False
    cnt = 0
    while flag == False:

        response = openai.ChatCompletion.create(engine="mtutor-openai-dev",
                                messages = messages,
                                temperature=0.5,)

        try:
            res = response["choices"][0]["message"]["content"]
            flag = True
        except:
            flag = False
        cnt += 1
        if cnt >= 3:
            break
    if flag == False:
        response = openai.ChatCompletion.create(engine="mtutor-openai-dev",
                                messages = messages,
                                temperature=0.5,)

        try:
            res = response["choices"][0]["message"]["content"]
        except:
            import pdb
            pdb.set_trace()
    return  res

def multi_chat(input_list, reply_list, role = None):
    
    if role is None:
        role = "You are an AI assistant that helps people find information."
    messages = [
                {"role":"system","content":role}
                ]
    for i in range(len(reply_list)):
        messages.append({"role":"user","content":input_list[i]})
        messages.append({"role":"assistant","content":reply_list[i]})
    messages.append({"role":"user","content":input_list[-1]})
    
    # print("\033[1;34;40mMuilt-Conversation Input:\033[0m",end=" ")
    # print(messages)

    response = openai.ChatCompletion.create(engine="mtutor-openai-dev",
                            messages = messages,
                            temperature=0,)
    
    res = response["choices"][0]["message"]["content"]


    return res

if __name__ == "__main__":
    content = '''
    You are playing a game of Werewolf.
    You are an werewolf, what should you do during the night.
    '''
    res = single_chat(content=content)
    print(res)