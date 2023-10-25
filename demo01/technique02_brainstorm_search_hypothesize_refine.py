import openai
import requests
import json

# Initialize main hypothesis and evidence list
main_query = input('What is your primary information query? ')
main_hypothesis = ""
evidence = []

# Define the system messages for brainstorming and hypothesis generation
brainstorm_system_message = "The USER will pass you a general purpose query or problem. You must generate a JSON list of search queries that will be used to search the internet for relevant information. Your output must be exclusively a JSON list. Make sure you search for multiple perspectives in order to get a well-rounded cross section."
hypothesis_system_message = "You are a hypothesis generator. You will be given a main query and a list of search results from the internet. Your output is to be a hypothesis - a proposed answer to the question."

# Define the function to search Wikipedia
def search_wikipedia(query):
    url = 'https://en.wikipedia.org/w/api.php'
    search_params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'format': 'json'
    }

    response = requests.get(url, params=search_params)
    data = response.json()

    # Get the title of the first result
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

    # Get the page ID of the first page
    page_id = list(data['query']['pages'].keys())[0]

    # Get the content of the page
    content = data['query']['pages'][page_id]['extract']

    # Get the URL of the page
    url = f"https://en.wikipedia.org/?curid={page_id}"

    return content, url



def chatbot(conversation, model="gpt-4", temperature=0, max_tokens=2000):
    max_retry = 7
    retry = 0
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
            sleep(5)
            if retry >= max_retry:
                exit()


# Define the function to use the ChatGPT API
def use_chatgpt(system_message, user_message):
    conversation = list()
    conversation.append({'role': 'system', 'content': system_message})
    conversation.append({'role': 'user', 'content': user_message})
    response, tokens = chatbot(conversation)
    return response
    

# Main loop
while True:
    # Step 1: Brainstorm a list of search queries
    search_queries_json = use_chatgpt(brainstorm_system_message, main_question)
    search_queries = json.loads(search_queries_json)

    # Step 2: Search the internet
    search_results = []
    search_urls = []
    for query in search_queries:
        content, url = search_wikipedia(query)
        search_results.append(content)
        search_urls.append(url)

    # Step 3: Generate a hypothesis
    new_hypothesis = use_chatgpt(hypothesis_system_message, f"Main Question: {main_question}\n\n\nArticles:\n\n{\n\n.join(search_results)}"

    # Step 4: Compare the new hypothesis to the original and update accordingly
    # ... (this will depend on how you want to compare and update the hypotheses)

    # Step 5: Accumulate the evidence
    for i in range(len(search_results)):
        evidence.append({"source": search_urls[i], "notes": search_results[i]})

    # Query satisfied test
    if query_satisfied(new_hypothesis, main_hypothesis):  # You'll need to define this function
        break

    # Update the main hypothesis
    main_hypothesis = new_hypothesis