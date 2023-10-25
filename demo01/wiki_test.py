import requests

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

    # Print the content of the page
    results = data['query']['pages'][page_id]['extract']
    return results

search_wikipedia('Python programming')