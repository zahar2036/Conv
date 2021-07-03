from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Rectangle

from kivy.core.window import Window

#Параметры окна:
Window.size = (456, 858)
Window.clearcolor = (245/255, 245/255, 245/255, 1)
#Window.clearcolor = (28/255, 28/255, 28/255, 1)

Builder.unload_file('rate.kv')

#Парсер и библиотеки для парса:
import requests
import re
from bs4 import BeautifulSoup

URL = 'https://myfin.by/currency/minsk'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
			'accept': '*/*'}
click = 0

class Container(GridLayout):
	def change_text(self):

		def get_html(url, params=None):
			r = requests.get(url, headers=HEADERS, params=params)
			return r

		def get_content(html):
			soup = BeautifulSoup(html, 'html.parser')
			items = soup.find('div', class_ = 'best-rates big-rates-table')
			items_td = items.find_all('td')
			book = []
			beek = {}
			k1 = 0
			k2 = 0
			index = 1

			#Алгоритмы фильтрации и добавления в словарь(beek):
			for item in items_td:
				book.append(item.text.strip())

			for i in book:
				if k2 % 5 == 0:
					k2 += 1
					continue
				else:	
					i = (i[:6])
					book[k2] = i
					k2 += 1	
				
			for a in range(5):
				beek[index] = []
				c = []
				for b in range(5):
					beek[index].append(book[k1])
					k1 += 1
				index += 1	

			#Распределине информации по лейблам для страницы Rate:
			stroka1 = beek[1]
			stroka2 = beek[2]
			stroka3 = beek[3]
			stroka4 = beek[4]
			stroka5 = beek[5]

			self.label_widget01.text = 'Валюта'
			self.label_widget02.text = 'Покупка'
			self.label_widget03.text = 'Продажа'
			self.label_widget04.text = 'НБ РБ'
			self.label_widget05.text = 'БВФБ'
			self.label_widget1.text = '$USD'
			self.label_widget2.text = stroka1[1]
			self.label_widget3.text = stroka1[2]
			self.label_widget4.text = stroka1[3]
			self.label_widget5.text = str(float(stroka1[4]))
			self.label_widget6.text = '€EUR'
			self.label_widget7.text = stroka2[1]
			self.label_widget8.text = stroka2[2]
			self.label_widget9.text = stroka2[3]
			self.label_widget10.text = stroka2[4]
			self.label_widget11.text = '₽RUB'
			self.label_widget12.text = stroka3[1]
			self.label_widget13.text = stroka3[2]
			self.label_widget14.text = stroka3[3]
			self.label_widget15.text = stroka3[4]
			self.label_widget16.text = 'złPLN'
			self.label_widget17.text = stroka4[1]
			self.label_widget18.text = stroka4[2]
			self.label_widget19.text = stroka4[3]
			self.label_widget20.text = stroka4[4]
			self.label_widget21.text = '₴UAH'
			self.label_widget22.text = stroka5[1]
			self.label_widget23.text = stroka5[2]
			self.label_widget24.text = stroka5[3]
			self.label_widget25.text = stroka5[4]

		#Получение Html-кода:
		def parse():
			html = get_html(URL)

			if html.status_code == 200:
				get_content(html.text)
			else:
				print('Error')

		parse()	

	#Отслеживание нажатий на кнопки Rate и Conv в спиннере:
	def rate_clicked(self, value):
		if value == 'Rate':
			click = 0
		elif value == 'Conv':
			click = 1

class Converter(Screen):
	pass

class RateApp(App):
	def build(self):
    	
    	 return Container()
		

#Запуск приложения
if __name__ == '__main__':
	RateApp().run()