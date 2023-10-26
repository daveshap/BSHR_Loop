from utils import use_chatgpt, get_system_message
import json

def satisfice(user_query, notes, queries, hypothesis):

    system_message = get_system_message("system03_satisficing_check.txt")

    user_message = (
f"""# USER QUERY
{user_query}


# NOTES
{notes}


# QUERIES AND ANSWERS
{queries}


# FINAL HYPOTHESIS
{hypothesis}

"""
    )

    response, tokens = use_chatgpt(system_message=system_message, user_message=user_message)

    feedback = json.loads(response)

    return feedback["satisficed"], feedback["feedback"], tokens
    