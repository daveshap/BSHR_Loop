from utils import get_system_message, use_chatgpt

def refine(notes):
    system_message = get_system_message("system04_spr_refine.txt")

    user_message = notes

    response, tokens = use_chatgpt(system_message, user_message)

    return response, tokens
