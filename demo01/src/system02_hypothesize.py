from utils import use_chatgpt, get_system_message

def hypothesize(user_query: str, notes: str, hypotheses: str):

    system_message = get_system_message('system02_hypothesize.txt')
    user_message = (
f"""
# USER QUERY
{user_query}


# NOTES
{notes}


# PREVIOUS HYPOTHISES
{hypotheses}
"""
    )
    response, tokens = use_chatgpt(system_message, user_message)
    print("new hypothesis: " + response)

    return response, tokens

        