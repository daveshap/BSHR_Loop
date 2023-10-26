import requests
import time
import sys
import random
from termcolor import colored
import pathlib
import openai
from halo import Halo
import time
import settings


def chatbot(conversation, model="gpt-4", temperature=0, max_tokens=2000):
    max_retry = 7
    retry = 0
    openai.api_key = settings.OPENAI_API_KEY

    while True:
        try:
            spinner = Halo(text='Thinking...', spinner='dots')
            spinner.start()
            
            response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
            text = response['choices'][0]['message']['content']

            spinner.stop()
            
            return text, response['usage']['total_tokens']
        except Exception as oops:
            retry += 1
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            time.sleep(5)
            if retry >= max_retry:
                exit()


# Define the function to use the ChatGPT API
def use_chatgpt(system_message, user_message):
    conversation = list()
    conversation.append({'role': 'system', 'content': system_message})
    conversation.append({'role': 'user', 'content': user_message})
    response, tokens = chatbot(conversation)
    return response, tokens

def search_wikipedia(query: str) -> (str, str):

    spinner = Halo(text='Information Foraging...', spinner='dots')
    spinner.start()

    url = 'https://en.wikipedia.org/w/api.php'
    search_params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'format': 'json'
    }

    response = requests.get(url, params=search_params)
    data = response.json()

    title = data['query']['search'][0]['title']

    content_params = {
        'action': 'query',
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
        'titles': title,
        'format': 'json'
    }

    response = requests.get(url, params=content_params)
    data = response.json()

    page_id = list(data['query']['pages'].keys())[0]

    content = data['query']['pages'][page_id]['extract']

    url = f"https://en.wikipedia.org/?curid={page_id}"

    spinner.stop()

    return content, url


def get_system_message(file_name: str):

    # assume the prompt are in the demo root for demo purposes
    demo_root = pathlib.Path(__file__).parent.parents[0]
    prompt_file_path = demo_root / file_name
 

    # Check if the file exists before trying to read it
    if prompt_file_path.exists() and prompt_file_path.is_file():
        # Open and read the file
        with open(prompt_file_path, 'r') as f:
            content = f.read()
        return content
    else:
        raise ValueError(f"The file {prompt_file_path} does not exist.")

