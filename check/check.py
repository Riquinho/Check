# coding=UTF-8
import urllib
import telepot

print (urllib.request.urlopen("https://labma.ufrj.br/site/").getcode())
print (urllib.request.urlopen("http://www.im.ufrj.br/index.php/pt/").getcode())
print (urllib.request.urlopen("http://www.poli.ufrj.br/").getcode())
print (urllib.request.urlopen("https://www.ct.ufrj.br/").getcode())
print (urllib.request.urlopen("https://ufrj.br/").getcode())
print (urllib.request.urlopen("https://labma.ufrj.br/SOGo/").getcode())


bot = telepot.Bot("991123381:AAEEwpegfFX2fTVu5rOrnL9ErmnIK8hHz0k")
bot.sendMessage(334165673,'Olá Riquinho, seu bandejão está agendado.')
