import random

def cnpj(cnpj):

	random.seed(cnpj)

	if '.' in cnpj:
		cnpj = cnpj.replace('.','')
		cnpj = cnpj.replace('/','')
		cnpj = cnpj.replace('-','')
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
	i = 0
	j = 0
	k = 0
	l = 1

	m = (a*5 + b*4 +c*3 + d*2 + e*9 + f*8 + g*7 + h*6 + i*5 +j*4 + k*3 + l*2)%11

	if m < 2:
		m = 0
	else:
		m = 11 - m

	n = (a*6 + b*5 +c*4 + d*3 + e*2 + f*9 + g*8 + h*7 + i*6 +j*5 + k*4 + l*3 + m*2)%11

	if n < 2:
		n = 0
	else:
		n = 11 - n


	if p == 's':
		CNPJ = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
	elif p == 'c':
		CNPJ = '{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}'.format(a,b,c,d,e,f,g,h,i,j,k,l,m,n)

	print(CNPJ)



cnpj('11444777000161')

cnpj('10213630000106')

cnpj('18781203000120')

cnpj('11222333000100')

cnpj('01.430.235/0001-86')

cnpj('43.044.947/0001-07')

cnpj('94.210.425/0001-79')

cnpj('19.939.723/0001-89')
