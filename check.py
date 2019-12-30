# coding=UTF-8
from urllib.request import urlopen
import time as t
import telepot
from telepot.loop import MessageLoop
from datetime import datetime

bot = telepot.Bot("991123381:AAEEwpegfFX2fTVu5rOrnL9ErmnIK8hHz0k")


def handle(msg):

	if msg['text'] == '/help' or msg['text'] == '/start':
		bot.sendMessage(-334165673,'Olá' + msg['from']['first_name'] + ', sou um bot desenvolvido pelo João Victor de check list dos sites da UFRJ, faço check a cada 6hs ou pelo comando /check')
	
	if msg['text'] == '/check':
		check(msg['from']['first_name'])


now= datetime.now()
today06 = now.replace(hour=6, minute=0, second=0, microsecond=0)
today18 = now.replace(hour=18, minute=0, second=0, microsecond=0)
today12 = now.replace(hour=12, minute=0, second=0, microsecond=0)
today00 = now.replace(hour=00, minute=0, second=0, microsecond=0)


def check(name):

	try:
		labma = urlopen("https://labma.ufrj.br/site/",timeout=5).getcode()
	except:
		labma = 404
		
	try:
		im = urlopen("http://www.im.ufrj.br/index.php/pt/",timeout=5).getcode()
	except:
		im = 404

	try:
		poli = urlopen("http://www.poli.ufrj.br/",timeout=5).getcode()
	except:
		poli = 404

	try:
		ct = urlopen("https://www.ct.ufrj.br/",timeout=5).getcode()
	except:
		ct = 404

	try:
		ufrj = urlopen("https://ufrj.br/",timeout=5).getcode()
	except:
		ufrj = 404

	try:
		email = urlopen("https://labma.ufrj.br/SOGo/",timeout=5).getcode()
	except:
		email = 404


	labma = '*OK*' if labma == 200 else '*ERRO*'
	im = '*OK*' if im == 200 else '*ERRO*'
	poli = '*OK*' if poli == 200 else '*ERRO*'
	ct = '*OK*' if ct == 200 else '*ERRO*'
	ufrj = '*OK*' if ufrj == 200 else '*ERRO*'
	email = '*OK*' if email == 200 else '*ERRO*'

	bot.sendMessage(-334165673,'Olá '+name+',\n\nSite do LABMA: ' + labma + '\nSite do IM: ' + im +'\nSite da POLI: ' + poli + '\nSite do CT: ' + ct + '\nSite da UFRJ: ' + ufrj + '\nSite do EMAIL:' + email+'\n\nDuvidas ou sugestôes, fale com o desenvolvedor: João Victor',  parse_mode= 'Markdown')



MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

if now ==today06 or now == today00 or now == today12 or now == today18:
	check('Check - Automatico')

while 1:
    t.sleep(10)



