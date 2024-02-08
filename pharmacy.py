import sys
from io import BytesIO
import requests
from PIL import Image
import pygame
from find_params import find_params
from find_distance import find_distance

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
address_ll = sys.argv[1]

search_params = {
    "apikey": api_key,
    "text": "Аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    print('Похоже, что-то пошло не так. Попробуйте повторить запрос')
    sys.exit()

pharmacy_address = response.json()['features'][0]['properties']['description']
pharmacy_name = response.json()['features'][0]['properties']['name']
pharmacy_hours = response.json()['features'][0]['properties']['CompanyMetaData']['Hours']['text']
pharmacy_coords = ','.join([str(i) for i in response.json()['features'][0]['geometry']['coordinates']])

dist_api_server = "https://api.routing.yandex.net/v2/distancematrix"
response = requests.get(dist_api_server, find_distance(address_ll, pharmacy_coords))
print(response.json())

map_params = find_params(response, address_ll)
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
sprite_group = pygame.sprite.Group()
map_sprite = pygame.sprite.Sprite()
map_sprite.image = pygame.image.frombytes(response.content, (600, 450), "RGB")
map_sprite.rect = map_sprite.image.get_rect()
map_sprite.rect.x = 0
map_sprite.rect.y = 0


font = pygame.font.Font(None, 20)


running = True
while running:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




dist_api_server = "https://api.routing.yandex.net/v2/distancematrix"
response

# Image.open(BytesIO(response.content)).save('map.png')

