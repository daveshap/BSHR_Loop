from utils import get_system_message, use_chatgpt, search_wikipedia
import json

def brainstorm(user_query: str, notes: str, queries: str):

    system_message = get_system_message('system01_brainstorm_search_queries.txt')
    user_message = (
f"""
# USER QUERY
{user_query}


# NOTES
{notes}


# PREVIOUS QUERIES
{queries}
"""
    )
    
    response, tokens = use_chatgpt(system_message, user_message)

    print(f"tokens used = {tokens}")
    print(f"new questions = {response}")
    questions = json.loads(response)

    for question in questions:
        content, url = search_wikipedia(question)
        notes = f"{notes}\n\nURL: {url}\nNOTE: {content}"
        queries = (
f"""
{queries}

QUESTION: {question}

"""
        )
    
    return queries, notes, tokens

