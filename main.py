#импортируем модули
import requests
#переменные и данные, для отправки запросов
URL = 'https://api.pokemonbattle.ru/v2' #хост и версия
TOKEN = '' # токен (нужно ввести свой)
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN} #хедеры

#переменные для body,что бы не усложнять строку с запросом
#body для регестрации тренера
body_registration = {
    "trainer_token": TOKEN, #переменная с токеном тренера
    "email": "", #нужно ввести свою почту
    "password":"" #нужно ввести пороль (свой, придуманный)
}
#body для активации тренера
body_confirmation = {
    "trainer_token": TOKEN #переменная с токеном тренера
}
#body для создания покемона
body_create = {
    "name": "generate", #имя покемона
    "photo_id":"-1"     #аватар покемона
}

#регистрация тренера
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''
#активация тренера
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''
#создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)
#сохранения значения ключа полученного в ответе, позволяет увидить боди ответа (будет видно не только статус код но и ответ из боди)
message = response_create.json()['message']
print(message)

