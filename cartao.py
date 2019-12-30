import random

american = 34 or 37
visa = 4
mastercard = 51 or 55


def cartao(cartao):

	random.seed(cartao)
	#adaptado para america express, visa e mastercard
	#maioria dos digitos verificadores ficam nos 2 primeiros, mantemos para continuar na mesma bandeira
	print(cartao)
	a = int(cartao[0])
	b = int(cartao[1])
	c = random.randint(0,9)
	d = random.randint(0,9)
	e = random.randint(0,9)
	f = random.randint(0,9)
	g = random.randint(0,9)
	h = random.randint(0,9)
	i = random.randint(0,9)
	j = random.randint(0,9)
	k = random.randint(0,9)
	l = random.randint(0,9)
	m = random.randint(0,9)
	
		


	a2 = sum(int(i) for i in (str(a*2)))
	c2 = sum(int(i) for i in (str(c*2)))
	e2 = sum(int(i) for i in (str(e*2)))
	g2 = sum(int(i) for i in (str(g*2)))
	i2 = sum(int(i) for i in (str(i*2)))
	k2 = sum(int(i) for i in (str(k*2)))
	m2 = sum(int(i) for i in (str(m*2)))
		
	#alguns cartoes possuem 15 a 16 digitos
	if len(cartao) == 14:
		p = 10 - ((a2+b+c2+d+e2+f+g2+h+i2+j+k2+l+m2)%10)
		
	elif len(cartao) == 15: 
		n = random.randint(0,9)
		p = 10 - ((a2+b+c2+d+e2+f+g2+h+i2+j+k2+l+m2+n)%10)

	elif len(cartao) == 16:
		n = random.randint(0,9)
		o = random.randint(0,9)
		o2 = sum(int(i) for i in (str(o*2)))
		p = 10 - ((a2+b+c2+d+e2+f+g2+h+i2+j+k2+l+m2+n+o2)%10)


	if p == 10:
		p = 0


	if len(cartao) == 14:
		cartao = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(a,b,c,d,e,f,g,h,i,j,k,l,m,p)
	elif len(cartao) == 15:
		cartao = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,p)
	elif len(cartao) == 16:
		cartao = '{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
	print(cartao)

cartao('4556058983937176')
print('----')
cartao('4024007188841448')
print('----')

cartao('4119512813483843')
print('----')

cartao('4929990638798530')