import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '9166d34e3e871acb210db6eb297434f9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "masha.galashina@yandex.ru",
    "password": "Mariua41514"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "pokemon_id": "27478",
    "name": "Рокки",
    "photo": "https://dolnikov.ru/pokemons/albums/306.png"
}

body = {
    "pokemon_id": "16297"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_cofirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_cofirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body)
print(response.text)