
def find_max(vote:dict):
    mx = 0
    final_name = ""
    for name,num in dict:
        if num > mx:
            mx = num
            final_name = name
    return final_name