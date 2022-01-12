def valida_int(pergunta, min, max):
	x = int(input(pergunta))
	while((x < min) or (x > max)):
		x = int(input(pergunta))
	return x

def fatorial(num):
	"""
	Calculo de fatorial
	:param num:
	:return: fatoial
	"""
	fat = 1
	if num == 0:
		return fat

	for i in range(1,num+1,1):
		fat *= i # fatorial recebe ela mesma * i // fat = fat * i

	return fat

#main
x = valida_int('Digite um valor para calcular o fatorial:', 0, 999999999)
print('{}! = {}'.format(x,fatorial(x)))

