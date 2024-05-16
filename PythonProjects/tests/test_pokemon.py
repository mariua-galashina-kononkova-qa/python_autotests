import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '9166d34e3e871acb210db6eb297434f9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = '2468'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Роки'
    
    
@pytest.mark.parametrize('key, value', [('name', 'Роки'), ('trainer_id', TRAINER_ID), ('id', '27478')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value