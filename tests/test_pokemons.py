#импортируем модули
import requests
import pytest
#переменные и данные, для отправки запросов
URL = 'https://api.pokemonbattle.ru/v2' #хост и версия
TOKEN = '' # токен (нужно ввести свой)
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN} #хедеры
TRAINER_ID = '' # тренер id (нужно ввести свой )

#каждый тест должен начинаться с test_
def test_status_code(): #тест на статус код 200
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200, 'Unexpected status code'

def test_part_of_response(): #тест на имя покемона
     response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID} )
     assert response_get.json()['data'][0]["name"] == 'dratini', 'another name'

#фикстура,передает параметры в функцию, которые нужны во время запуска тестов
@pytest.mark.parametrize('key, value', [('name', 'dratini'), ('trainer_id', TRAINER_ID), ('id', '69414')]) 
def test_parametrize(key, value): #проверка id покемона
     response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
     assert response_parametrize.json()["data"][0][key] == value, 'Unexpected id code'