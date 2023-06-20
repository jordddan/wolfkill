import openai
import os
from utils.key import key
os.environ["OPENAI_API_KEY"] = key
openai.api_type = "azure"

openai.api_base = "https://mtutor-dev.openai.azure.com/"

openai.api_version = "2023-03-15-preview"

openai.api_key = os.getenv("OPENAI_API_KEY")

def single_chat(content,role=None):


    if role is None:
        role = "You are an AI assistant that helps people find information."
    messages = [
                {"role":"system","content":role},
                {"role":"user","content":content}
                ]

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