import random

def rg(rg):

	random.seed(rg)

	if '.' in rg:
		rg = rg.replace('.','')
		rg = rg.replace('-','')
		p = 'c'
	else:
		p = 's'

	a = random.randint(0,9)
	b = random.randint(0,9)
	c = random.randint(0,9)
	d = random.randint(0,9)
	e = random.randint(0,9)
	f = random.randint(0,9)
	g = random.randint(0,9)
	h = random.randint(0,9)
	

	i = (a*2 + b*3 +c*4 + d*5 + e*6 + f*7 + g*8 + h*9)%11

	i = 11 - i

	if i == 11:
		i = 0
	elif i == 10:
		i = 'X'  #  certo e X, alguns sites aceitam 1 ,verificar, nao sei se funciona
		

	if p == 's':
		RG = '{}{}{}{}{}{}{}{}{}'.format(a,b,c,d,e,f,g,h,i)
	elif p == 'c':
		RG = '{}{}.{}{}{}.{}{}{}-{}'.format(a,b,c,d,e,f,g,h,i)

	print(RG)



rg('360562577')

rg('392556935')

rg('478261986')

rg('299697046')

rg('49.865.114-9')

rg('12.992.500-7')

rg('19.824.848-9')

rg('45.859.911-6')
