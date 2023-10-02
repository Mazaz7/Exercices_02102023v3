import requests
try:
    # Make an API request to the Dad Jokes API
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

    # Check if the response status code indicates success (200 OK)
    if response.status_code == 200:
        # Parse the JSON response to retrieve the joke
        data = response.json()
        joke = data['joke']
        print(f"Dad Joke: {joke}")
    else:
        print(f"API request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    # Handle network-related exceptions (e.g., no internet connection)
    print(f"An error occurred: {e}")
except Exception as e:
    # Handle other exceptions
    print(f"An unexpected error occurred: {e}")
