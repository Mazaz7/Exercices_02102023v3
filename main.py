import requests
try:
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

    if response.status_code == 200:
        # Parse the JSON response to retrieve the joke
        data = response.json()
        joke = data['joke']
        print(f"Dad Joke: {joke}")
    else:
        print(f"API request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
"What is this change"
