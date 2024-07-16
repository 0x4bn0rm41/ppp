import os, json, time
from pathlib import Path
from datetime import datetime
import base64
import string, random
import requests as rq
from pprint import pprint
import urllib

asn = 'https://www.whatismyip.com/asn/country/ru/'
def gen_boxberry(i):
	digit_len = 7, 9
	digit_len = 3,2,3,5
	string_len = 3
	for x in range(i):
		s = ''.join(random.choices(string.ascii_letters.lower(), k=string_len))
		d = ''.join(random.choices(string.digits, k=random.choice(digit_len)))
		dd = ''.join(random.choices(string.digits, k=random.choice(digit_len)))

		print(s+d)
		res = rq.get(f'https://boxberry.ru/api/v1/tracking/order/get?searchId={d+dd}').text
		pprint(res)
		time.sleep(.8)


def tg_channel_by_id(id = None):
	url = 'https://api.telegram.org/bot<token-here>?<api-method-here>'
	print(rq.get('https://api.telegram.org/bot1890629635:AAFLhRjuqaDYeZPMLtwCOaLZZCKzE7AtvF8/getChatMembersCount?chat_id=-1001615491316;').text)

# print(rq.get('https://api.telegram.org/bot1890629635:AAFLhRjuqaDYeZPMLtwCOaLZZCKzE7AtvF8/has_hidden_members?chat_id=@cryptomichelangelo').text)
png = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIW2P4qLHvAwAGrQLI+q60swAAAABJRU5ErkJggg=='
hexx = [x for x in base64.b64decode(png)]
# ascii = [ord(x) for x in hexx]
# print(ascii)
# for ch in hexx:
	# print([chr(ch)], ch)

# print(base64.b64encode(b'just interest, how u found  this :-)? '))
from html import unescape

# s = 'https://clicker.joincommunity.xyz/clicker#tgWebAppData=user%3D%257B%2522id%2522%253A1645505835%252C%2522first_name%2522%253A%2522Closed%2522%252C%2522last_name%2522%253A%2522Gateway%2522%252C%2522username%2522%253A%2522Closedgateway%2522%252C%2522language_code%2522%253A%2522ru%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26chat_instance%3D4039163761373577971%26chat_type%3Dsender%26auth_date%3D1705958372%26hash%3D6ca9266d47a55a6764d0d4a39f2ca47cfac95d075ec6947b21aba420d1c8a711&tgWebAppVersion=7.0&tgWebAppPlatform=web&tgWebAppBotInline=1&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212121%22%2C%22button_color%22%3A%22%238774e1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23aaaaaa%22%2C%22link_color%22%3A%22%238774e1%22%2C%22secondary_bg_color%22%3A%22%23181818%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23212121%22%2C%22accent_text_color%22%3A%22%238774e1%22%2C%22section_bg_color%22%3A%22%23212121%22%2C%22section_header_text_color%22%3A%22%238774e1%22%2C%22subtitle_text_color%22%3A%22%23aaaaaa%22%2C%22destructive_text_color%22%3A%22%23ff595a%22%7D'
# print(
# 	urllib.parse.unquote(s).replace('%7B', '{').replace('%22', '"').replace('%3A', ':').replace('%2C', ',').replace('%7D', '}')
# 	)

