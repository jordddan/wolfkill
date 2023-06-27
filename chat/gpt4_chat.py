import os

import openai

from utils.key import key

from func_timeout import func_set_timeout
openai.api_type = "azure"

openai.api_base = "https://mtutor-dev.openai.azure.com/"

openai.api_version = "2023-03-15-preview"

openai.api_key = key

 

# response = openai.ChatCompletion.create(
# engine="devgpt4-32k", # devgpt4 is 8k version
# messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"are you gpt4"}],
# temperature=0.7,
# max_tokens=800,
# top_p=0.95,
# frequency_penalty=0,
# presence_penalty=0,
# stop=None

@func_set_timeout(30)
def get_response(messages):
    response = openai.ChatCompletion.create(
        engine="devgpt4-32k", # devgpt4 is 8k version
        messages = messages,
        temperature=0.5)
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
        if cnt >= 10:
            break    
    if res == None:
        raise TypeError("GPT-4 Can not get the response.")
    return  res
