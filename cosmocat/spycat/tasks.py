import requests


def get_available_greeds(url) -> list:
    response = requests.get(url)
    breed_names = [breed["name"] for breed in response.json()]
    return breed_names


print(get_available_greeds("https://api.thecatapi.com/v1/breeds"))
